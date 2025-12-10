"""ESHealth API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/eshealth-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI
from pyarkime.models import ESHealth


class ESHealthAPI(BaseAPI):
    """Elasticsearch health API endpoint."""

    def get(self, **kwargs: Any) -> dict[str, Any]:
        """Get Elasticsearch health.

        GET - /api/eshealth

        Args:
            **kwargs: Additional parameters

        Returns:
            ESHealth object
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get("/api/eshealth", params=params)
        return self._handle_response(response)


class AsyncESHealthAPI(BaseAPI):
    """Async ESHealth API endpoint."""

    async def get(self, **kwargs: Any) -> dict[str, Any]:
        """Get Elasticsearch health (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get("/api/eshealth", params=params)
        return self._handle_response(response)

