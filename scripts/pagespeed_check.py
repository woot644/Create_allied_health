"""
pagespeed_check.py — PageSpeed Insights + CrUX via the PSI API.
Usage: python pagespeed_check.py <url> [--strategy mobile|desktop] [--json]
"""

import json
import sys
import argparse
import urllib.request
import urllib.parse
import os

GOOGLE_API_CONFIG = os.path.expanduser("~/.config/claude-seo/google-api.json")

def load_api_key():
    try:
        with open(GOOGLE_API_CONFIG) as f:
            return json.load(f).get("api_key", "")
    except Exception:
        return ""


def run_psi(url, strategy="mobile", api_key=""):
    params = {
        "url":      url,
        "strategy": strategy,
        "category": ["performance", "accessibility", "best-practices", "seo"],
        "key":       api_key,
    }
    # category is multi-value — build manually
    base = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?"
    parts = []
    for k, v in params.items():
        if isinstance(v, list):
            for item in v:
                parts.append(f"{k}={urllib.parse.quote(str(item))}")
        else:
            parts.append(f"{k}={urllib.parse.quote(str(v))}")
    full_url = base + "&".join(parts)
    req = urllib.request.Request(full_url)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def extract_cwv(data):
    """Pull CrUX field data from PSI response."""
    cwv = {}
    lhr = data.get("lighthouseResult", {})
    categories = lhr.get("categories", {})
    audits = lhr.get("audits", {})

    cwv["performance_score"] = int((categories.get("performance", {}).get("score") or 0) * 100)
    cwv["accessibility_score"] = int((categories.get("accessibility", {}).get("score") or 0) * 100)
    cwv["best_practices_score"] = int((categories.get("best-practices", {}).get("score") or 0) * 100)
    cwv["seo_score"] = int((categories.get("seo", {}).get("score") or 0) * 100)

    # Lab metrics
    metrics = {
        "lcp":   "largest-contentful-paint",
        "fcp":   "first-contentful-paint",
        "tbt":   "total-blocking-time",
        "cls":   "cumulative-layout-shift",
        "si":    "speed-index",
        "tti":   "interactive",
    }
    cwv["lab"] = {}
    for key, audit_id in metrics.items():
        audit = audits.get(audit_id, {})
        cwv["lab"][key] = {
            "display": audit.get("displayValue", "N/A"),
            "score":   audit.get("score"),
            "numeric": audit.get("numericValue"),
        }

    # CrUX field data
    field = data.get("loadingExperience", {})
    cwv["field"] = {}
    cwv["field_overall"] = field.get("overall_category", "N/A")
    metric_map = {
        "LCP": "LARGEST_CONTENTFUL_PAINT_MS",
        "INP": "INTERACTION_TO_NEXT_PAINT",
        "CLS": "CUMULATIVE_LAYOUT_SHIFT_SCORE",
        "FCP": "FIRST_CONTENTFUL_PAINT_MS",
        "TTFB": "EXPERIMENTAL_TIME_TO_FIRST_BYTE",
    }
    metrics_data = field.get("metrics", {})
    for label, key in metric_map.items():
        m = metrics_data.get(key, {})
        if m:
            p75 = m.get("percentile", "N/A")
            category = m.get("category", "N/A")
            cwv["field"][label] = {"p75": p75, "category": category}

    return cwv


def rating(metric, value):
    """Return traffic-light rating string."""
    if value is None:
        return "N/A"
    thresholds = {
        "LCP":  (2500, 4000),
        "INP":  (200,  500),
        "CLS":  (0.1,  0.25),
        "FCP":  (1800, 3000),
        "TTFB": (800,  1800),
    }
    if metric not in thresholds:
        return "N/A"
    good, poor = thresholds[metric]
    if value <= good:
        return "GOOD"
    elif value <= poor:
        return "NEEDS IMPROVEMENT"
    else:
        return "POOR"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--strategy", default="mobile", choices=["mobile", "desktop"])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    api_key = load_api_key()
    try:
        data = run_psi(args.url, args.strategy, api_key)
        cwv  = extract_cwv(data)
        result = {
            "url":      args.url,
            "strategy": args.strategy,
            "scores":   {
                "performance":     cwv["performance_score"],
                "accessibility":   cwv["accessibility_score"],
                "best_practices":  cwv["best_practices_score"],
                "seo":             cwv["seo_score"],
            },
            "lab_metrics": cwv["lab"],
            "field_data":  cwv["field"],
            "field_overall": cwv["field_overall"],
            "data_source": "Google PageSpeed Insights API (field data: CrUX 28-day rolling)",
            "status": "success",
        }
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"URL: {args.url} [{args.strategy}]")
            print(f"Performance: {cwv['performance_score']}/100")
            for m, v in cwv["field"].items():
                print(f"  {m}: {v['p75']}  ({v['category']})")
    except Exception as e:
        err = {"status": "error", "url": args.url, "error": str(e)}
        if args.json:
            print(json.dumps(err, indent=2))
        else:
            print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
