"""Low-level HTTP helpers for the exchange API."""
from __future__ import annotations

import os
import time
import hmac
import hashlib
import json
from typing import Any, Dict, Optional

import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("EXCHANGE_BASE_URL")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET", "")

DEFAULT_SESSION = requests.Session()
DEFAULT_SESSION.headers.update({"Content-Type": "application/json"})


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
    body_obj: Optional[Dict[str, Any]] = None,
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

    body_str = ""
    if body_obj is not None:
        body_str = json.dumps(body_obj, separators=(",", ":"), ensure_ascii=False)

    payload = f"{timestamp}{method_upper}{request_path}{body_str}"
    signature = hmac.new(
        api_secret.encode("utf-8"),
        payload.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()

    return {
        "X-CH-APIKEY": api_key,
        "X-CH-TS": timestamp,
        "X-CH-SIGN": signature,
        "Content-Type": "application/json",
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
    headers = sign_headers(
        "POST",
        request_path,
        body,
        api_key=api_key,
        api_secret=api_secret,
    )
    response = session.post(
        url,
        headers=headers,
        data=json.dumps(body, ensure_ascii=False),
        timeout=10,
    )
    response.raise_for_status()
    return response.json()
