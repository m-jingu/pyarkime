"""ESIndices API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/esindices-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI


class ESIndicesAPI(BaseAPI):
    """Elasticsearch indices API endpoint."""

    def list(self, **kwargs: Any) -> list[dict[str, Any]]:
        """List Elasticsearch indices.

        GET - /api/esindices

        Args:
            **kwargs: Additional parameters

        Returns:
            List of index objects
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get("/api/esindices", params=params)
        result = self._handle_response(response)
        if isinstance(result, list):
            return result
        return []

    def get(self, index_name: str, **kwargs: Any) -> dict[str, Any]:
        """Get index information.

        GET - /api/esindices/:index

        Args:
            index_name: Index name
            **kwargs: Additional parameters

        Returns:
            Index information
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get(f"/api/esindices/{index_name}", params=params)
        return self._handle_response(response)

    def optimize(self, index_name: str, **kwargs: Any) -> dict[str, Any]:
        """Optimize an index.

        POST - /api/esindices/:index/optimize

        Args:
            index_name: Index name
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.post(f"/api/esindices/{index_name}/optimize", json=params)
        return self._handle_response(response)

    def close(self, index_name: str, **kwargs: Any) -> dict[str, Any]:
        """Close an index.

        POST - /api/esindices/:index/close

        Args:
            index_name: Index name
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.post(f"/api/esindices/{index_name}/close", json=params)
        return self._handle_response(response)

    def open(self, index_name: str, **kwargs: Any) -> dict[str, Any]:
        """Open an index.

        POST - /api/esindices/:index/open

        Args:
            index_name: Index name
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.post(f"/api/esindices/{index_name}/open", json=params)
        return self._handle_response(response)

    def shrink(self, index_name: str, **kwargs: Any) -> dict[str, Any]:
        """Shrink an index.

        POST - /api/esindices/:index/shrink

        Args:
            index_name: Index name
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.post(f"/api/esindices/{index_name}/shrink", json=params)
        return self._handle_response(response)


class AsyncESIndicesAPI(BaseAPI):
    """Async ESIndices API endpoint."""

    async def list(self, **kwargs: Any) -> list[dict[str, Any]]:
        """List Elasticsearch indices (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get("/api/esindices", params=params)
        result = self._handle_response(response)
        if isinstance(result, list):
            return result
        return []

    async def get(self, index_name: str, **kwargs: Any) -> dict[str, Any]:
        """Get index information (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get(f"/api/esindices/{index_name}", params=params)
        return self._handle_response(response)

    async def optimize(self, index_name: str, **kwargs: Any) -> dict[str, Any]:
        """Optimize an index (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.post(f"/api/esindices/{index_name}/optimize", json=params)
        return self._handle_response(response)

    async def close(self, index_name: str, **kwargs: Any) -> dict[str, Any]:
        """Close an index (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.post(f"/api/esindices/{index_name}/close", json=params)
        return self._handle_response(response)

    async def open(self, index_name: str, **kwargs: Any) -> dict[str, Any]:
        """Open an index (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.post(f"/api/esindices/{index_name}/open", json=params)
        return self._handle_response(response)

    async def shrink(self, index_name: str, **kwargs: Any) -> dict[str, Any]:
        """Shrink an index (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.post(f"/api/esindices/{index_name}/shrink", json=params)
        return self._handle_response(response)

