"""FieldActions API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/fieldactions-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI


class FieldActionsAPI(BaseAPI):
    """FieldActions API endpoint."""

    def get(self, **kwargs: Any) -> dict[str, Any]:
        """Get field actions.

        GET - /api/fieldactions

        Args:
            **kwargs: Additional parameters

        Returns:
            Field actions object
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get("/api/fieldactions", params=params)
        return self._handle_response(response)


class AsyncFieldActionsAPI(BaseAPI):
    """Async FieldActions API endpoint."""

    async def get(self, **kwargs: Any) -> dict[str, Any]:
        """Get field actions (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get("/api/fieldactions", params=params)
        return self._handle_response(response)

