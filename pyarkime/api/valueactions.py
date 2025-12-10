"""ValueActions API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/valueactions-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI


class ValueActionsAPI(BaseAPI):
    """ValueActions API endpoint."""

    def get(self, **kwargs: Any) -> dict[str, Any]:
        """Get value actions.

        GET - /api/valueactions

        Args:
            **kwargs: Additional parameters

        Returns:
            Value actions object
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get("/api/valueactions", params=params)
        return self._handle_response(response)


class AsyncValueActionsAPI(BaseAPI):
    """Async ValueActions API endpoint."""

    async def get(self, **kwargs: Any) -> dict[str, Any]:
        """Get value actions (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get("/api/valueactions", params=params)
        return self._handle_response(response)

