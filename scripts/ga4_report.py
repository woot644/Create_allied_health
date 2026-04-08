"""
ga4_report.py — GA4 Data API reports via OAuth.
Usage:
  python ga4_report.py --property <id> [--json]                        # organic sessions (28d)
  python ga4_report.py --property <id> --report top-pages [--json]     # top organic landing pages
"""

import json
import sys
import argparse
import urllib.request
import urllib.parse
import os

OAUTH_TOKEN_PATH = os.path.expanduser("~/.config/claude-seo/oauth-token.json")
OAUTH_CREDS_PATH = os.path.expanduser("~/.config/google/credentials.json")
GOOGLE_API_CONFIG = os.path.expanduser("~/.config/claude-seo/google-api.json")


def load_token():
    import time
    try:
        with open(OAUTH_TOKEN_PATH) as f:
            token = json.load(f)
        expires_at = token.get("expires_at", 0)
        if time.time() > expires_at - 60:
            token = refresh_token(token)
        return token.get("access_token", "")
    except Exception as e:
        return ""


def refresh_token(token_data):
    import time
    try:
        with open(OAUTH_CREDS_PATH) as f:
            creds = json.load(f)
        payload = urllib.parse.urlencode({
            "client_id":     creds["installed"]["client_id"],
            "client_secret": creds["installed"]["client_secret"],
            "refresh_token": token_data["refresh_token"],
            "grant_type":    "refresh_token",
        }).encode()
        req = urllib.request.Request(
            "https://oauth2.googleapis.com/token",
            data=payload, method="POST"
        )
        with urllib.request.urlopen(req, timeout=10) as r:
            new_token = json.loads(r.read())
            token_data["access_token"] = new_token["access_token"]
            token_data["expires_at"]   = time.time() + new_token.get("expires_in", 3599)
            with open(OAUTH_TOKEN_PATH, "w") as f:
                json.dump(token_data, f, indent=2)
            return token_data
    except Exception as e:
        return token_data


def ga4_request(property_id, body, access_token):
    # Ensure property_id is in "properties/NNNN" format
    if not property_id.startswith("properties/"):
        property_id = f"properties/{property_id}"
    url = f"https://analyticsdata.googleapis.com/v1beta/{property_id}:runReport"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type":  "application/json",
    }
    data = json.dumps(body).encode()
    req  = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def organic_sessions_report(property_id, access_token):
    """28-day organic traffic summary with daily breakdown."""
    body = {
        "dateRanges": [{"startDate": "28daysAgo", "endDate": "today"}],
        "dimensions": [{"name": "date"}, {"name": "sessionDefaultChannelGroup"}],
        "metrics": [
            {"name": "sessions"},
            {"name": "totalUsers"},
            {"name": "bounceRate"},
            {"name": "averageSessionDuration"},
            {"name": "screenPageViewsPerSession"},
        ],
        "dimensionFilter": {
            "filter": {
                "fieldName": "sessionDefaultChannelGroup",
                "stringFilter": {"matchType": "EXACT", "value": "Organic Search"}
            }
        },
        "orderBys": [{"dimension": {"dimensionName": "date"}}],
        "limit": 30,
    }
    return ga4_request(property_id, body, access_token)


def top_pages_report(property_id, access_token):
    """Top organic landing pages by sessions (28 days)."""
    body = {
        "dateRanges": [{"startDate": "28daysAgo", "endDate": "today"}],
        "dimensions": [{"name": "landingPage"}, {"name": "sessionDefaultChannelGroup"}],
        "metrics": [
            {"name": "sessions"},
            {"name": "totalUsers"},
            {"name": "bounceRate"},
            {"name": "conversions"},
        ],
        "dimensionFilter": {
            "filter": {
                "fieldName": "sessionDefaultChannelGroup",
                "stringFilter": {"matchType": "EXACT", "value": "Organic Search"}
            }
        },
        "orderBys": [{"metric": {"metricName": "sessions"}, "desc": True}],
        "limit": 20,
    }
    return ga4_request(property_id, body, access_token)


def parse_rows(response):
    dim_headers = [h["name"] for h in response.get("dimensionHeaders", [])]
    met_headers = [h["name"] for h in response.get("metricHeaders", [])]
    rows = []
    for row in response.get("rows", []):
        r = {}
        for i, dv in enumerate(row.get("dimensionValues", [])):
            r[dim_headers[i]] = dv["value"]
        for i, mv in enumerate(row.get("metricValues", [])):
            r[met_headers[i]] = mv["value"]
        rows.append(r)
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--property", default="")
    parser.add_argument("--report",   default="organic", choices=["organic", "top-pages"])
    parser.add_argument("--json",     action="store_true")
    args = parser.parse_args()

    # Load property from config if not given
    prop = args.property
    if not prop:
        try:
            with open(GOOGLE_API_CONFIG) as f:
                cfg = json.load(f)
            prop = cfg.get("ga4_property_id", "")
        except Exception:
            pass

    if not prop:
        err = {"status": "error", "error": "--property is required (e.g. properties/123456789)"}
        print(json.dumps(err, indent=2) if args.json else err["error"])
        sys.exit(1)

    access_token = load_token()
    if not access_token:
        err = {"status": "error", "error": "No valid OAuth token available."}
        print(json.dumps(err, indent=2) if args.json else err["error"])
        sys.exit(1)

    try:
        if args.report == "organic":
            raw  = organic_sessions_report(prop, access_token)
            rows = parse_rows(raw)
            # Summarise totals
            total_sessions = sum(int(r.get("sessions", 0)) for r in rows)
            total_users    = sum(int(r.get("totalUsers", 0)) for r in rows)
            result = {
                "status":          "success",
                "property":        prop,
                "report":          "organic_sessions_28d",
                "totals": {
                    "sessions": total_sessions,
                    "users":    total_users,
                },
                "daily_rows":      rows,
                "data_source":     "Google Analytics 4 API (1-day lag)",
                "note":            "Filtered to Organic Search channel only",
            }
        else:
            raw  = top_pages_report(prop, access_token)
            rows = parse_rows(raw)
            result = {
                "status":      "success",
                "property":    prop,
                "report":      "top_organic_landing_pages_28d",
                "pages":       rows,
                "data_source": "Google Analytics 4 API (1-day lag)",
                "note":        "Filtered to Organic Search channel, ordered by sessions desc",
            }

        print(json.dumps(result, indent=2) if args.json else str(result))

    except urllib.error.HTTPError as e:
        body = e.read().decode()
        err  = {"status": "error", "property": prop, "http_status": e.code, "error": body}
        print(json.dumps(err, indent=2) if args.json else err["error"])
    except Exception as e:
        err = {"status": "error", "error": str(e)}
        print(json.dumps(err, indent=2) if args.json else err["error"])


if __name__ == "__main__":
    main()
