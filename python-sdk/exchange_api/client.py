"""High-level Exchange client built on top of the HTTP helpers."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional

from . import http
from .base import BaseClient
from .futures import FuturesClient

if TYPE_CHECKING:
    import requests


class ExchangeClient(BaseClient):
    """Convenience wrapper that exposes common exchange API endpoints."""

    def __init__(
        self,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        session: Optional["requests.Session"] = None,
        futures_client: Optional[FuturesClient] = None,
    ) -> None:
        resolved_base_url = base_url or http.BASE_URL or "https://openapi.yourdomain.com"
        resolved_api_key = api_key if api_key is not None else http.API_KEY
        resolved_api_secret = api_secret if api_secret is not None else http.API_SECRET

        super().__init__(
            resolved_base_url,
            api_key=resolved_api_key,
            api_secret=resolved_api_secret,
            session=session,
        )
        self.futures = futures_client or FuturesClient(
            session=self.session,
            api_key=self._api_key,
            api_secret=self._api_secret,
        )

    # Example higher-level wrappers. Extend following docs as needed.
    def ping(self) -> Any:
        return self._public_get("/sapi/v2/ping")

    def server_time(self) -> Any:
        return self._public_get("/sapi/v2/time")

    def ticker(self, symbol: str) -> Any:
        return self._public_get("/sapi/v2/ticker", params={"symbol": symbol})

    def account(self) -> Any:
        return self._private_get("/sapi/v1/account")

    def order_test(self, body: Dict[str, Any]) -> Any:
        return self._private_post("/sapi/v2/order/test", body)
