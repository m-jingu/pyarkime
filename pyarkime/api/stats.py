"""Stats API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/stats-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI


class StatsAPI(BaseAPI):
    """Stats API endpoint."""

    def get_stats(self, **kwargs: Any) -> dict[str, Any]:
        """Get stats.

        GET - /api/stats

        Args:
            **kwargs: Additional parameters

        Returns:
            Stats object
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get("/api/stats", params=params)
        return self._handle_response(response)

    def get_dstats(self, **kwargs: Any) -> dict[str, Any]:
        """Get dstats.

        GET - /api/dstats

        Args:
            **kwargs: Additional parameters

        Returns:
            Dstats object
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get("/api/dstats", params=params)
        return self._handle_response(response)

    def get_esstats(self, **kwargs: Any) -> dict[str, Any]:
        """Get Elasticsearch stats.

        GET - /api/esstats

        Args:
            **kwargs: Additional parameters

        Returns:
            ES stats object
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get("/api/esstats", params=params)
        return self._handle_response(response)


class AsyncStatsAPI(BaseAPI):
    """Async Stats API endpoint."""

    async def get_stats(self, **kwargs: Any) -> dict[str, Any]:
        """Get stats (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get("/api/stats", params=params)
        return self._handle_response(response)

    async def get_dstats(self, **kwargs: Any) -> dict[str, Any]:
        """Get dstats (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get("/api/dstats", params=params)
        return self._handle_response(response)

    async def get_esstats(self, **kwargs: Any) -> dict[str, Any]:
        """Get Elasticsearch stats (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get("/api/esstats", params=params)
        return self._handle_response(response)

