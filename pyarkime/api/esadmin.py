"""ESAdmin API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/esadmin-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI


class ESAdminAPI(BaseAPI):
    """Elasticsearch admin API endpoint."""

    def get(self, **kwargs: Any) -> dict[str, Any]:
        """Get Elasticsearch admin info.

        GET - /api/esadmin

        Args:
            **kwargs: Additional parameters

        Returns:
            ES admin info
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get("/api/esadmin", params=params)
        return self._handle_response(response)

    def set(self, **kwargs: Any) -> dict[str, Any]:
        """Set Elasticsearch settings.

        POST - /api/esadmin/set

        Args:
            **kwargs: Settings to set

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.post("/api/esadmin/set", json=params)
        return self._handle_response(response)

    def reroute(self, **kwargs: Any) -> dict[str, Any]:
        """Reroute shards.

        POST - /api/esadmin/reroute

        Args:
            **kwargs: Reroute parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.post("/api/esadmin/reroute", json=params)
        return self._handle_response(response)

    def flush(self, **kwargs: Any) -> dict[str, Any]:
        """Flush indices.

        POST - /api/esadmin/flush

        Args:
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.post("/api/esadmin/flush", json=params)
        return self._handle_response(response)

    def unflood(self, **kwargs: Any) -> dict[str, Any]:
        """Unflood stage.

        POST - /api/esadmin/unflood

        Args:
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.post("/api/esadmin/unflood", json=params)
        return self._handle_response(response)

    def clear_cache(self, **kwargs: Any) -> dict[str, Any]:
        """Clear cache.

        POST - /api/esadmin/clearcache

        Args:
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.post("/api/esadmin/clearcache", json=params)
        return self._handle_response(response)


class AsyncESAdminAPI(BaseAPI):
    """Async ESAdmin API endpoint."""

    async def get(self, **kwargs: Any) -> dict[str, Any]:
        """Get Elasticsearch admin info (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get("/api/esadmin", params=params)
        return self._handle_response(response)

    async def set(self, **kwargs: Any) -> dict[str, Any]:
        """Set Elasticsearch settings (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.post("/api/esadmin/set", json=params)
        return self._handle_response(response)

    async def reroute(self, **kwargs: Any) -> dict[str, Any]:
        """Reroute shards (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.post("/api/esadmin/reroute", json=params)
        return self._handle_response(response)

    async def flush(self, **kwargs: Any) -> dict[str, Any]:
        """Flush indices (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.post("/api/esadmin/flush", json=params)
        return self._handle_response(response)

    async def unflood(self, **kwargs: Any) -> dict[str, Any]:
        """Unflood stage (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.post("/api/esadmin/unflood", json=params)
        return self._handle_response(response)

    async def clear_cache(self, **kwargs: Any) -> dict[str, Any]:
        """Clear cache (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.post("/api/esadmin/clearcache", json=params)
        return self._handle_response(response)

