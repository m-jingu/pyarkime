"""ESRecovery API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/esrecovery-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI


class ESRecoveryAPI(BaseAPI):
    """Elasticsearch recovery API endpoint."""

    def get(self, **kwargs: Any) -> dict[str, Any]:
        """Get Elasticsearch recovery info.

        GET - /api/esrecovery

        Args:
            **kwargs: Additional parameters

        Returns:
            Recovery info
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get("/api/esrecovery", params=params)
        return self._handle_response(response)


class AsyncESRecoveryAPI(BaseAPI):
    """Async ESRecovery API endpoint."""

    async def get(self, **kwargs: Any) -> dict[str, Any]:
        """Get Elasticsearch recovery info (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get("/api/esrecovery", params=params)
        return self._handle_response(response)

