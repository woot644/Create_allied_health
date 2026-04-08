"""
google_auth.py — Checks available Google API credentials and reports tier.

Tier 0: API key present (PSI + CrUX)
Tier 1: API key + OAuth token with webmasters scope (+ GSC)
Tier 2: Tier 1 + analytics.readonly scope (+ GA4)
"""

import json
import os
import sys
import time
import argparse

GOOGLE_API_CONFIG = os.path.expanduser("~/.config/claude-seo/google-api.json")
OAUTH_TOKEN_PATH  = os.path.expanduser("~/.config/claude-seo/oauth-token.json")
OAUTH_CREDS_PATH  = os.path.expanduser("~/.config/google/credentials.json")


def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return None


def refresh_token(creds, token_data):
    """Attempt to refresh the OAuth access token using the refresh token."""
    import urllib.request
    import urllib.parse
    payload = urllib.parse.urlencode({
        "client_id":     creds["installed"]["client_id"],
        "client_secret": creds["installed"]["client_secret"],
        "refresh_token": token_data["refresh_token"],
        "grant_type":    "refresh_token",
    }).encode()
    req = urllib.request.Request(
        "https://oauth2.googleapis.com/token",
        data=payload,
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            new_token = json.loads(r.read())
            token_data["access_token"] = new_token["access_token"]
            token_data["expires_at"]   = time.time() + new_token.get("expires_in", 3599)
            with open(OAUTH_TOKEN_PATH, "w") as f:
                json.dump(token_data, f, indent=2)
            return token_data
    except Exception as e:
        return None


def check():
    result = {"tier": 0, "api_key": False, "oauth": False, "scopes": [], "errors": []}

    api_cfg = load_json(GOOGLE_API_CONFIG)
    if api_cfg and api_cfg.get("api_key"):
        result["api_key"]   = True
        result["api_key_value"] = api_cfg["api_key"]
        result["gsc_property"]  = api_cfg.get("default_property", "")
        result["ga4_property"]  = api_cfg.get("ga4_property_id", "")
        result["tier"]          = max(result["tier"], 0)

    token_data = load_json(OAUTH_TOKEN_PATH)
    if token_data:
        # Check expiry
        expires_at = token_data.get("expires_at", 0)
        if time.time() > expires_at - 60:
            creds = load_json(OAUTH_CREDS_PATH)
            if creds:
                token_data = refresh_token(creds, token_data)
                if not token_data:
                    result["errors"].append("OAuth token expired and refresh failed.")

        if token_data:
            scopes = token_data.get("scope", "").split()
            result["oauth"]        = True
            result["access_token"] = token_data["access_token"]
            result["scopes"]       = scopes
            if "https://www.googleapis.com/auth/webmasters" in scopes:
                result["tier"] = max(result["tier"], 1)
            if "https://www.googleapis.com/auth/analytics.readonly" in scopes:
                result["tier"] = max(result["tier"], 2)

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--json",  action="store_true")
    args = parser.parse_args()

    result = check()
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Tier: {result['tier']}")
        print(f"API Key: {result['api_key']}")
        print(f"OAuth:   {result['oauth']}")
        print(f"Scopes:  {result['scopes']}")
        if result["errors"]:
            print("Errors:")
            for e in result["errors"]:
                print(f"  - {e}")
