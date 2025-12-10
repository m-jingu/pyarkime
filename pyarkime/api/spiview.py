"""SPIView API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/spiview-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI


class SPIViewAPI(BaseAPI):
    """SPIView API endpoint."""

    def get(self, **kwargs: Any) -> dict[str, Any]:
        """Get SPIView data.

        POST/GET - /api/spiview

        Args:
            **kwargs: Query parameters

        Returns:
            SPIView data
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get("/api/spiview", params=params)
        return self._handle_response(response)


class AsyncSPIViewAPI(BaseAPI):
    """Async SPIView API endpoint."""

    async def get(self, **kwargs: Any) -> dict[str, Any]:
        """Get SPIView data (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get("/api/spiview", params=params)
        return self._handle_response(response)

