"""ESShards API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/esshards-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI


class ESShardsAPI(BaseAPI):
    """Elasticsearch shards API endpoint."""

    def exclude(
        self, shard_type: str, shard_value: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Exclude a shard.

        POST - /api/esshards/:type/:value/exclude

        Args:
            shard_type: Shard type
            shard_value: Shard value
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.post(
            f"/api/esshards/{shard_type}/{shard_value}/exclude", json=params
        )
        return self._handle_response(response)

    def include(
        self, shard_type: str, shard_value: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Include a shard.

        POST - /api/esshards/:type/:value/include

        Args:
            shard_type: Shard type
            shard_value: Shard value
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.post(
            f"/api/esshards/{shard_type}/{shard_value}/include", json=params
        )
        return self._handle_response(response)

    def delete(
        self, index_name: str, shard_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Delete a shard.

        POST - /api/esshards/:index/:shard/delete

        Args:
            index_name: Index name
            shard_id: Shard ID
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.post(
            f"/api/esshards/{index_name}/{shard_id}/delete", json=params
        )
        return self._handle_response(response)


class AsyncESShardsAPI(BaseAPI):
    """Async ESShards API endpoint."""

    async def exclude(
        self, shard_type: str, shard_value: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Exclude a shard (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.post(
            f"/api/esshards/{shard_type}/{shard_value}/exclude", json=params
        )
        return self._handle_response(response)

    async def include(
        self, shard_type: str, shard_value: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Include a shard (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.post(
            f"/api/esshards/{shard_type}/{shard_value}/include", json=params
        )
        return self._handle_response(response)

    async def delete(
        self, index_name: str, shard_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Delete a shard (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.post(
            f"/api/esshards/{index_name}/{shard_id}/delete", json=params
        )
        return self._handle_response(response)

