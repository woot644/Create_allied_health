"""
gsc_inspect.py — Google Search Console URL Inspection API.
Usage: python gsc_inspect.py <url> --property <prop> [--json]
"""

import json
import sys
import argparse
import urllib.request
import urllib.parse
import os

OAUTH_TOKEN_PATH = os.path.expanduser("~/.config/claude-seo/oauth-token.json")
OAUTH_CREDS_PATH = os.path.expanduser("~/.config/google/credentials.json")


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


def inspect_url(page_url, site_url, access_token):
    endpoint = "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect"
    body     = {
        "inspectionUrl": page_url,
        "siteUrl":       site_url,
    }
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type":  "application/json",
    }
    data = json.dumps(body).encode()
    req  = urllib.request.Request(endpoint, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def parse_inspection(raw):
    result = raw.get("inspectionResult", {})
    index  = result.get("indexStatusResult", {})
    mobile = result.get("mobileUsabilityResult", {})
    rich   = result.get("richResultsResult", {})

    return {
        "verdict":               index.get("verdict", "N/A"),
        "coverage_state":        index.get("coverageState", "N/A"),
        "robots_txt_state":      index.get("robotsTxtState", "N/A"),
        "indexing_state":        index.get("indexingState", "N/A"),
        "page_fetch_state":      index.get("pageFetchState", "N/A"),
        "last_crawl_time":       index.get("lastCrawlTime", "N/A"),
        "crawled_as":            index.get("crawledAs", "N/A"),
        "canonical_google":      index.get("googleCanonical", "N/A"),
        "canonical_user":        index.get("userCanonical", "N/A"),
        "sitemap":               index.get("sitemap", []),
        "mobile_verdict":        mobile.get("verdict", "N/A"),
        "mobile_issues":         mobile.get("issues", []),
        "rich_results_verdict":  rich.get("verdict", "N/A"),
        "rich_results_items":    rich.get("detectedItems", []),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--property", default="")
    parser.add_argument("--json",  action="store_true")
    args = parser.parse_args()

    access_token = load_token()
    if not access_token:
        err = {"status": "error", "error": "No valid OAuth token available."}
        print(json.dumps(err, indent=2) if args.json else err["error"])
        sys.exit(1)

    # Derive site URL from property (sc-domain: or https://)
    prop = args.property
    if not prop:
        # Try to infer from the URL
        from urllib.parse import urlparse
        p = urlparse(args.url)
        prop = f"sc-domain:{p.netloc.lstrip('www.')}"

    try:
        raw    = inspect_url(args.url, prop, access_token)
        parsed = parse_inspection(raw)
        result = {
            "status":   "success",
            "url":      args.url,
            "property": prop,
            "inspection": parsed,
            "data_source": "Google Search Console URL Inspection API",
        }
        print(json.dumps(result, indent=2) if args.json else str(parsed))
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        err  = {"status": "error", "url": args.url, "http_status": e.code, "error": body}
        print(json.dumps(err, indent=2) if args.json else err["error"])
    except Exception as e:
        err = {"status": "error", "url": args.url, "error": str(e)}
        print(json.dumps(err, indent=2) if args.json else err["error"])


if __name__ == "__main__":
    main()
