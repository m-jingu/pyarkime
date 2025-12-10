"""Crons API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/crons-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI
from pyarkime.models import ArkimeQuery


class CronsAPI(BaseAPI):
    """Crons (periodic queries) API endpoint."""

    def list(self, **kwargs: Any) -> list[dict[str, Any]]:
        """List all periodic queries.

        GET - /api/crons

        Args:
            **kwargs: Additional parameters

        Returns:
            List of query objects
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get("/api/crons", params=params)
        result = self._handle_response(response)
        if isinstance(result, list):
            return result
        return []

    def create(
        self, query: ArkimeQuery | dict[str, Any], **kwargs: Any
    ) -> dict[str, Any]:
        """Create a new periodic query.

        POST - /api/cron

        Args:
            query: Query object or dict
            **kwargs: Additional parameters

        Returns:
            Created query object
        """
        if isinstance(query, ArkimeQuery):
            query_dict = query.model_dump(exclude_none=True)
        else:
            query_dict = query
        params = self._prepare_params(**query_dict, **kwargs)
        response = self._client.post("/api/cron", json=params)
        return self._handle_response(response)

    def update(
        self, query_key: str, query: ArkimeQuery | dict[str, Any], **kwargs: Any
    ) -> dict[str, Any]:
        """Update a periodic query.

        POST - /api/cron/:key

        Args:
            query_key: Query key
            query: Query object or dict
            **kwargs: Additional parameters

        Returns:
            Updated query object
        """
        if isinstance(query, ArkimeQuery):
            query_dict = query.model_dump(exclude_none=True)
        else:
            query_dict = query
        params = self._prepare_params(**query_dict, **kwargs)
        response = self._client.post(f"/api/cron/{query_key}", json=params)
        return self._handle_response(response)

    def delete(self, query_key: str, **kwargs: Any) -> dict[str, Any]:
        """Delete a periodic query.

        DELETE - /api/cron/:key

        Args:
            query_key: Query key
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.delete(f"/api/cron/{query_key}", params=params)
        return self._handle_response(response)


class AsyncCronsAPI(BaseAPI):
    """Async Crons API endpoint."""

    async def list(self, **kwargs: Any) -> list[dict[str, Any]]:
        """List all periodic queries (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get("/api/crons", params=params)
        result = self._handle_response(response)
        if isinstance(result, list):
            return result
        return []

    async def create(
        self, query: ArkimeQuery | dict[str, Any], **kwargs: Any
    ) -> dict[str, Any]:
        """Create a new periodic query (async)."""
        if isinstance(query, ArkimeQuery):
            query_dict = query.model_dump(exclude_none=True)
        else:
            query_dict = query
        params = self._prepare_params(**query_dict, **kwargs)
        response = await self._client.post("/api/cron", json=params)
        return self._handle_response(response)

    async def update(
        self, query_key: str, query: ArkimeQuery | dict[str, Any], **kwargs: Any
    ) -> dict[str, Any]:
        """Update a periodic query (async)."""
        if isinstance(query, ArkimeQuery):
            query_dict = query.model_dump(exclude_none=True)
        else:
            query_dict = query
        params = self._prepare_params(**query_dict, **kwargs)
        response = await self._client.post(f"/api/cron/{query_key}", json=params)
        return self._handle_response(response)

    async def delete(self, query_key: str, **kwargs: Any) -> dict[str, Any]:
        """Delete a periodic query (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.delete(f"/api/cron/{query_key}", params=params)
        return self._handle_response(response)

