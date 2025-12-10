"""Fields API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/fields-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI


class FieldsAPI(BaseAPI):
    """Fields API endpoint."""

    def list(self, **kwargs: Any) -> dict[str, Any]:
        """List all fields.

        GET - /api/fields

        Args:
            **kwargs: Additional parameters

        Returns:
            Fields object
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get("/api/fields", params=params)
        return self._handle_response(response)


class AsyncFieldsAPI(BaseAPI):
    """Async Fields API endpoint."""

    async def list(self, **kwargs: Any) -> dict[str, Any]:
        """List all fields (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get("/api/fields", params=params)
        return self._handle_response(response)

