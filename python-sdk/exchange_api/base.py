"""Shared client functionality for exchange HTTP access."""
from __future__ import annotations

from typing import Any, Dict, Optional

import requests

from . import http


class BaseClient:
    """Base client that handles session management and signed requests."""

    def __init__(
        self,
        base_url: str,
        *,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        session: Optional[requests.Session] = None,
    ) -> None:
        self.base_url = base_url
        self._api_key = api_key
        self._api_secret = api_secret
        self.session = session or requests.Session()
        self.session.headers.setdefault("Content-Type", "application/json")

    @staticmethod
    def _filter_params(data: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        if data is None:
            return None
        return {k: v for k, v in data.items() if v is not None}

    def has_credentials(self) -> bool:
        """Return True if both API key and secret are available."""
        return bool(self._api_key and self._api_secret)

    def _public_get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """Call a public endpoint."""
        return http.get(
            path,
            self._filter_params(params),
            base_url=self.base_url,
            session=self.session,
        )

    def _private_get(self, path: str, query: Optional[Dict[str, Any]] = None) -> Any:
        """Call a signed GET endpoint."""
        return http.private_get(
            path,
            self._filter_params(query),
            base_url=self.base_url,
            api_key=self._api_key,
            api_secret=self._api_secret,
            session=self.session,
        )

    def _private_post(self, path: str, body: Optional[Dict[str, Any]] = None) -> Any:
        """Call a signed POST endpoint."""
        payload = self._filter_params(body or {})
        return http.private_post(
            path,
            payload or {},
            base_url=self.base_url,
            api_key=self._api_key,
            api_secret=self._api_secret,
            session=self.session,
        )
