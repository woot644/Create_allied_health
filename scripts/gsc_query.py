"""
gsc_query.py — Google Search Console queries via the Search Analytics API.
Usage:
  python gsc_query.py --property <prop> [--json]            # top queries + pages
  python gsc_query.py sitemaps --property <prop> [--json]   # sitemap list
  python gsc_query.py list-properties [--json]              # list all verified properties
"""

import json
import sys
import argparse
import urllib.request
import urllib.parse
import os

OAUTH_TOKEN_PATH  = os.path.expanduser("~/.config/claude-seo/oauth-token.json")
OAUTH_CREDS_PATH  = os.path.expanduser("~/.config/google/credentials.json")


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
        print(f"Token load error: {e}", file=sys.stderr)
        return ""


def refresh_token(token_data):
    import time
    try:
        with open(OAUTH_CREDS_PATH) as f:
            creds = json.load(f)
        import urllib.parse
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
        print(f"Refresh error: {e}", file=sys.stderr)
        return token_data


def gsc_request(endpoint, method="GET", body=None, access_token=""):
    headers = {"Authorization": f"Bearer {access_token}"}
    if body:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode()
    else:
        data = None
    req = urllib.request.Request(endpoint, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def list_properties(access_token):
    url  = "https://www.googleapis.com/webmasters/v3/sites"
    resp = gsc_request(url, access_token=access_token)
    return resp.get("siteEntry", [])


def search_analytics(property_url, dimensions, start_date, end_date, row_limit, access_token):
    enc  = urllib.parse.quote(property_url, safe="")
    url  = f"https://www.googleapis.com/webmasters/v3/sites/{enc}/searchAnalytics/query"
    body = {
        "startDate":  start_date,
        "endDate":    end_date,
        "dimensions": dimensions,
        "rowLimit":   row_limit,
        "startRow":   0,
    }
    return gsc_request(url, method="POST", body=body, access_token=access_token)


def get_sitemaps(property_url, access_token):
    enc = urllib.parse.quote(property_url, safe="")
    url = f"https://www.googleapis.com/webmasters/v3/sites/{enc}/sitemaps"
    return gsc_request(url, access_token=access_token)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", nargs="?", default="analytics",
                        choices=["analytics", "sitemaps", "list-properties"])
    parser.add_argument("--property", default="")
    parser.add_argument("--start", default="")
    parser.add_argument("--end",   default="")
    parser.add_argument("--rows",  type=int, default=25)
    parser.add_argument("--json",  action="store_true")
    args = parser.parse_args()

    from datetime import date, timedelta
    end_date   = args.end   or (date.today() - timedelta(days=3)).isoformat()
    start_date = args.start or (date.today() - timedelta(days=31)).isoformat()

    access_token = load_token()
    if not access_token:
        err = {"status": "error", "error": "No valid OAuth token available."}
        print(json.dumps(err, indent=2) if args.json else err["error"])
        sys.exit(1)

    if args.command == "list-properties":
        try:
            props = list_properties(access_token)
            result = {"status": "success", "properties": props}
            print(json.dumps(result, indent=2) if args.json else str(props))
        except Exception as e:
            err = {"status": "error", "error": str(e)}
            print(json.dumps(err, indent=2) if args.json else err["error"])
        return

    prop = args.property
    if not prop:
        err = {"status": "error", "error": "--property is required for this command."}
        print(json.dumps(err, indent=2) if args.json else err["error"])
        sys.exit(1)

    if args.command == "sitemaps":
        try:
            raw = get_sitemaps(prop, access_token)
            result = {"status": "success", "property": prop, "sitemaps": raw.get("sitemap", [])}
            print(json.dumps(result, indent=2) if args.json else str(raw))
        except urllib.error.HTTPError as e:
            body = e.read().decode()
            err  = {"status": "error", "http_status": e.code, "error": body}
            print(json.dumps(err, indent=2) if args.json else err["error"])
        except Exception as e:
            err = {"status": "error", "error": str(e)}
            print(json.dumps(err, indent=2) if args.json else err["error"])
        return

    # Default: search analytics — queries + pages
    try:
        queries = search_analytics(prop, ["query"], start_date, end_date, args.rows, access_token)
        pages   = search_analytics(prop, ["page"],  start_date, end_date, args.rows, access_token)
        result  = {
            "status":     "success",
            "property":   prop,
            "date_range": {"start": start_date, "end": end_date},
            "top_queries": queries.get("rows", []),
            "top_pages":   pages.get("rows", []),
            "data_source": "Google Search Console API (2-3 day lag)",
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
