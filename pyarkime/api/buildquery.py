"""BuildQuery API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/buildquery-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI


class BuildQueryAPI(BaseAPI):
    """BuildQuery API endpoint."""

    def build(self, **kwargs: Any) -> dict[str, Any]:
        """Build query.

        POST/GET - /api/buildquery

        Args:
            **kwargs: Query parameters

        Returns:
            Built query object
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get("/api/buildquery", params=params)
        return self._handle_response(response)


class AsyncBuildQueryAPI(BaseAPI):
    """Async BuildQuery API endpoint."""

    async def build(self, **kwargs: Any) -> dict[str, Any]:
        """Build query (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get("/api/buildquery", params=params)
        return self._handle_response(response)

