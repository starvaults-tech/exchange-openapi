"""Low-level HTTP helpers for the exchange API."""
from __future__ import annotations

import os
import time
import hmac
import hashlib
import json
from typing import Any, Dict, Optional
from collections import OrderedDict

import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("EXCHANGE_BASE_URL")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET", "")

DEFAULT_SESSION = requests.Session()
DEFAULT_SESSION.headers.update({"Content-Type": "application/json"})

def canonical_json(obj: dict) -> str:
    # ordered = OrderedDict(sorted(obj.items()))
    ordered = obj.copy()
    return json.dumps(ordered, separators=(",", ":"), ensure_ascii=False)

def get(
    path: str,
    params: Optional[Dict[str, Any]] = None,
    *,
    base_url: Optional[str] = None,
    session: Optional[requests.Session] = None,
) -> Any:
    """Perform a public GET request and return the JSON response."""
    base_url = base_url or BASE_URL
    session = session or DEFAULT_SESSION
    url = f"{base_url}{path}"
    response = session.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def sign_headers(
    method: str,
    request_path: str,
    body_str: str = "",
    *,
    api_key: Optional[str] = None,
    api_secret: Optional[str] = None,
) -> Dict[str, str]:
    """
    Generate the required authentication headers for private endpoints.
    The signature schema follows: HMAC_SHA256(secret, timestamp + method + requestPath + body)
    """
    timestamp = str(int(time.time() * 1000))
    api_key = api_key or API_KEY
    api_secret = api_secret or API_SECRET
    method_upper = method.upper()
    payload = f"{timestamp}{method_upper}{request_path}{body_str}"
    signature = hmac.new(
        api_secret.encode("utf-8"),
        payload.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()

    return {
        "X-CH-TS": timestamp,
        "X-CH-APIKEY": api_key,
        "X-CH-SIGN": signature,
        "Content-Type": "application/json",
        "futures-version": "101"
    }


def private_get(
    path: str,
    query: Optional[Dict[str, Any]] = None,
    *,
    base_url: Optional[str] = None,
    api_key: Optional[str] = None,
    api_secret: Optional[str] = None,
    session: Optional[requests.Session] = None,
) -> Any:
    """Perform a signed GET request used for private endpoints."""
    base_url = base_url or BASE_URL
    session = session or DEFAULT_SESSION
    request_path = path
    if query:
        query_string = urlencode(query, doseq=True)
        request_path = f"{path}?{query_string}"
        url = f"{base_url}{request_path}"
    else:
        url = f"{base_url}{path}"

    headers = sign_headers(
        "GET",
        request_path,
        api_key=api_key,
        api_secret=api_secret,
    )
    response = session.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()


def private_post(
    path: str,
    body: Dict[str, Any],
    *,
    base_url: Optional[str] = None,
    api_key: Optional[str] = None,
    api_secret: Optional[str] = None,
    session: Optional[requests.Session] = None,
) -> Any:
    """Perform a signed POST request used for private endpoints."""
    base_url = base_url or BASE_URL
    session = session or DEFAULT_SESSION
    request_path = path
    url = f"{base_url}{request_path}"

    body_str = canonical_json(body)

    headers = sign_headers(
        "POST",
        request_path,
        body_str,
        api_key=api_key,
        api_secret=api_secret,
    )
    response = session.post(
        url,
        headers=headers,
        data=body_str,
        timeout=10,
    )
    response.raise_for_status()
    return response.json()
