"""Histories API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/histories-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI
from pyarkime.models import History


class HistoriesAPI(BaseAPI):
    """Histories API endpoint."""

    def list(self, **kwargs: Any) -> list[dict[str, Any]]:
        """List histories.

        GET - /api/histories

        Args:
            **kwargs: Additional parameters

        Returns:
            List of history objects
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get("/api/histories", params=params)
        result = self._handle_response(response)
        if isinstance(result, list):
            return result
        return []

    def get(self, history_id: str, **kwargs: Any) -> dict[str, Any]:
        """Get history by ID.

        GET - /api/history/:id

        Args:
            history_id: History ID
            **kwargs: Additional parameters

        Returns:
            History object
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get(f"/api/history/{history_id}", params=params)
        return self._handle_response(response)


class AsyncHistoriesAPI(BaseAPI):
    """Async Histories API endpoint."""

    async def list(self, **kwargs: Any) -> list[dict[str, Any]]:
        """List histories (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get("/api/histories", params=params)
        result = self._handle_response(response)
        if isinstance(result, list):
            return result
        return []

    async def get(self, history_id: str, **kwargs: Any) -> dict[str, Any]:
        """Get history by ID (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get(f"/api/history/{history_id}", params=params)
        return self._handle_response(response)

