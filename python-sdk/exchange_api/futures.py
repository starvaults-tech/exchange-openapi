"""Futures-specific client wrapping the shared HTTP helpers."""
from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Optional

from . import http
from .base import BaseClient

if TYPE_CHECKING:
    import requests

FUTURES_BASE_URL = os.getenv("FUTURES_BASE_URL")
FUTURES_API_KEY = os.getenv("API_KEY", http.API_KEY)
FUTURES_API_SECRET = os.getenv("API_SECRET", http.API_SECRET)


class FuturesClient(BaseClient):
    """Client for interacting with the futures REST API."""

    def __init__(
        self,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        session: Optional["requests.Session"] = None,
    ) -> None:
        base_url = base_url or FUTURES_BASE_URL
        api_key = api_key if api_key is not None else FUTURES_API_KEY
        api_secret = api_secret if api_secret is not None else FUTURES_API_SECRET

        super().__init__(
            base_url=base_url,
            api_key=api_key,
            api_secret=api_secret,
            session=session,
        )

    # Public endpoints -----------------------------------------------------
    def ping(self) -> Any:
        """Test connectivity to the futures REST API."""
        return self._public_get("/fapi/v1/ping")

    def server_time(self) -> Any:
        """Fetch server time metadata."""
        return self._public_get("/fapi/v1/time")

    def contracts(self) -> Any:
        """List available futures contracts."""
        return self._public_get("/fapi/v1/contracts")

    def depth(
        self,
        contract_name: str,
        limit: Optional[int] = None,
    ) -> Any:
        """Get order book depth."""
        return self._public_get("/fapi/v1/depth", {
            "contractName": contract_name,
            "limit": limit,
        })

    def ticker(
        self,
        contract_name: str
    ) -> Any:
        """Get 24h ticker statistics."""
        return self._public_get("/fapi/v1/ticker", {
            "contractName": contract_name,
        })

    def ticker_all(self) -> Any:
        """Get ticker statistics for all contracts."""
        return self._public_get("/fapi/v1/ticker_all")

    def index_price(
        self,
        contract_name: str,
        limit: Optional[int] = None,
    ) -> Any:
        """Fetch index and mark price data."""
        return self._public_get("/fapi/v1/index", {
            "contractName": contract_name,
            "limit": limit,
        })

    def klines(
        self,
        contract_name: str,
        interval: str,
        limit: Optional[int] = None,
    ) -> Any:
        """Retrieve candlestick data."""
        payload = locals().copy()
        payload.pop("self", None)
        return self._public_get("/fapi/v1/klines", {
            "contractName": contract_name,
            "interval": interval,
            "limit": limit
        })

    # Trading endpoints ----------------------------------------------------
    def create_order(
        self,
        volume: float,
        contract_name: str,
        type: Literal["LIMIT", "MARKET"],
        side: Literal["BUY", "SELL"],
        open: Literal["OPEN", "CLOSE"],
        price: Optional[float] = None,
        position_type: Literal[1, 2] = 1,  # 1 Cross Margin, 2 Isolated Margin
        client_order_id: Optional[str] = None, # length < 32
        time_in_force: Optional[Literal["IOC", "FOK", "POST_ONLY", None]] = None,
        order_unit: int = 1,
    ) -> Any:
        """Create a futures order."""
        return self._private_post("/fapi/v1/order", {
            "positionType":1,
            "side":"BUY",
            "volume":0.1,
            "open":"OPEN",
            "type":"MARKET",
            "orderUnit":1,
            "contractName":"S-BTC-USDT"
        })

        return self._private_post("/fapi/v1/order", {
            "positionType" : position_type,
            "side" : side,
            "volume" : volume,
            "open" : open,
            "type" : type,
            "orderUnit" : order_unit,
            "price" : price,
            "contractName" : contract_name,
            "clientOrderId" : client_order_id,
            "timeInForce" : time_in_force,
        })

    def create_condition_order(
        self,
        volume: float,
        contract_name: str,
        type: Literal["LIMIT", "MARKET"],
        side: Literal["BUY", "SELL"],
        open: Literal["OPEN", "CLOSE"],
        triggerType: Literal["LIMIT", "MARKET"],
        triggerPrice: float,
        price: Optional[float] = None,
        position_type: Literal[1, 2] = 1,  # 1 Cross Margin, 2 Isolated Margin
        client_order_id: Optional[str] = None, # length < 32
    ) -> Any:
        """Create a conditional futures order."""
        return self._private_post("/fapi/v1/conditionOrder", body)

    def cancel_order(self, body: Dict[str, Any]) -> Any:
        """Cancel a specific order."""
        return self._private_post("/fapi/v1/cancel", body)

    def cancel_all_orders(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Cancel all orders, optionally filtered by payload parameters."""
        return self._private_post("/fapi/v1/cancel_all", body or {})

    def get_order(
        self,
        contract_name: str,
        order_id: Optional[str] = None,
        client_order_id: Optional[str] = None,
    ) -> Any:
        """Fetch order detail by identifiers."""
        params = {
            "contractName": contract_name,
            "orderId": order_id,
            "clientOrderId": client_order_id,
        }
        return self._private_get("/fapi/v1/order", params)

    def open_orders(
        self,
        contract_name: Optional[str] = None
    ) -> Any:
        """List current open orders."""
        params = {"contractName": contract_name} if contract_name else None
        return self._private_get("/fapi/v1/openOrders", params)

    def order_history(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Retrieve historical order records."""
        return self._private_post("/fapi/v1/orderHistorical", body or {})

    def profit_history(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Retrieve historical profit records."""
        return self._private_post("/fapi/v1/profitHistorical", body or {})

    def my_trades(
        self,
        contract_name: Optional[str] = None,
        limit: Optional[int] = None,
        from_id: Optional[int] = None,
    ) -> Any:
        """Retrieve trade history."""
        params = {"contractName": contract_name, "limit": limit, "fromId": from_id}
        return self._private_get("/fapi/v1/myTrades", params)

    def edit_user_position_model(self, body: Dict[str, Any]) -> Any:
        """Switch position mode."""
        return self._private_post("/fapi/v1/edit_user_position_model", body)

    def edit_user_margin_model(self, body: Dict[str, Any]) -> Any:
        """Switch margin mode."""
        return self._private_post("/fapi/v1/edit_user_margin_model", body)

    def edit_position_margin(self, body: Dict[str, Any]) -> Any:
        """Adjust position margin."""
        return self._private_post("/fapi/v1/edit_position_margin", body)

    def edit_lever(
        self,
        contract_name: str,
        now_level: int,
    ) -> Any:
        """Change leverage for a contract."""
        return self._private_post("/fapi/v1/edit_lever", {
            "nowLevel": now_level,
            "contractName": contract_name,
        })

    # Account endpoints ----------------------------------------------------
    def account(self) -> Any:
        """Fetch futures account balances and positions."""
        return self._private_get("/fapi/v1/account")
