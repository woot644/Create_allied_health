"""
crux_history.py — CrUX History API (28-day rolling windows over time).
Usage: python crux_history.py <url_or_origin> [--origin] [--json]
"""

import json
import sys
import argparse
import urllib.request
import os

GOOGLE_API_CONFIG = os.path.expanduser("~/.config/claude-seo/google-api.json")

def load_api_key():
    try:
        with open(GOOGLE_API_CONFIG) as f:
            return json.load(f).get("api_key", "")
    except Exception:
        return ""


def query_crux_history(url_or_origin, is_origin=False, api_key=""):
    endpoint = f"https://chromeuxreport.googleapis.com/v1/records:queryHistoryRecord?key={api_key}"
    if is_origin:
        payload = {"origin": url_or_origin, "metrics": [
            "largest_contentful_paint", "interaction_to_next_paint",
            "cumulative_layout_shift", "first_contentful_paint",
            "experimental_time_to_first_byte"
        ]}
    else:
        payload = {"url": url_or_origin, "metrics": [
            "largest_contentful_paint", "interaction_to_next_paint",
            "cumulative_layout_shift", "first_contentful_paint",
            "experimental_time_to_first_byte"
        ]}
    data = json.dumps(payload).encode()
    req  = urllib.request.Request(endpoint, data=data,
                                   headers={"Content-Type": "application/json"},
                                   method="POST")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def extract_latest(response):
    """Pull the most recent collection period data."""
    record   = response.get("record", {})
    metrics  = record.get("metrics", {})
    coll_periods = record.get("collectionPeriods", [])
    latest_period = coll_periods[-1] if coll_periods else {}

    result = {"collection_period": latest_period, "metrics": {}}
    metric_map = {
        "largest_contentful_paint":        "LCP",
        "interaction_to_next_paint":        "INP",
        "cumulative_layout_shift":          "CLS",
        "first_contentful_paint":           "FCP",
        "experimental_time_to_first_byte":  "TTFB",
    }

    thresholds = {
        "LCP":  (2500, 4000),
        "INP":  (200,  500),
        "CLS":  (0.1,  0.25),
        "FCP":  (1800, 3000),
        "TTFB": (800,  1800),
    }

    for raw_key, label in metric_map.items():
        m = metrics.get(raw_key, {})
        if not m:
            continue
        # p75 is the last element in the histogram percentilesTimeseries
        p75_series = m.get("percentilesTimeseries", {}).get("p75s", [])
        p75 = p75_series[-1] if p75_series else None

        # histogram (good/needs improvement/poor fractions) latest
        hist_series = m.get("histogramTimeseries", [])
        fractions = {}
        buckets = ["good", "needs_improvement", "poor"]
        for i, bucket in enumerate(hist_series):
            densities = bucket.get("densities", [])
            val = densities[-1] if densities else None
            fractions[buckets[i]] = round(val * 100, 1) if val is not None else None

        category = "N/A"
        if p75 is not None and label in thresholds:
            good_t, poor_t = thresholds[label]
            if p75 <= good_t:
                category = "GOOD"
            elif p75 <= poor_t:
                category = "NEEDS IMPROVEMENT"
            else:
                category = "POOR"

        result["metrics"][label] = {
            "p75":      p75,
            "category": category,
            "fractions": fractions,
        }

    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("target")
    parser.add_argument("--origin", action="store_true")
    parser.add_argument("--json",   action="store_true")
    args = parser.parse_args()

    api_key = load_api_key()
    try:
        raw    = query_crux_history(args.target, args.origin, api_key)
        parsed = extract_latest(raw)
        output = {
            "target":      args.target,
            "type":        "origin" if args.origin else "url",
            "data":        parsed,
            "data_source": "CrUX History API (28-day rolling)",
            "status":      "success",
        }
        if args.json:
            print(json.dumps(output, indent=2))
        else:
            print(f"CrUX {'Origin' if args.origin else 'URL'}: {args.target}")
            for m, v in parsed["metrics"].items():
                print(f"  {m}: p75={v['p75']}  [{v['category']}]")
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        err = {"status": "error", "target": args.target, "http_status": e.code, "error": body}
        if args.json:
            print(json.dumps(err, indent=2))
        else:
            print(f"HTTP {e.code}: {body}")
        sys.exit(1)
    except Exception as e:
        err = {"status": "error", "target": args.target, "error": str(e)}
        if args.json:
            print(json.dumps(err, indent=2))
        else:
            print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
