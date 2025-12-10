"""Unique API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/unique-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI


class UniqueAPI(BaseAPI):
    """Unique API endpoint."""

    def get(self, field: str, **kwargs: Any) -> dict[str, Any]:
        """Get unique values for a field.

        POST/GET - /api/unique

        Args:
            field: Field name
            **kwargs: Query parameters

        Returns:
            Unique values data
        """
        params = self._prepare_params(field=field, **kwargs)
        response = self._client.get("/api/unique", params=params)
        return self._handle_response(response)

    def multi(self, fields: list[str], **kwargs: Any) -> dict[str, Any]:
        """Get unique values for multiple fields.

        POST/GET - /api/multiunique

        Args:
            fields: List of field names
            **kwargs: Query parameters

        Returns:
            Multi-unique values data
        """
        params = self._prepare_params(fields=",".join(fields), **kwargs)
        response = self._client.get("/api/multiunique", params=params)
        return self._handle_response(response)


class AsyncUniqueAPI(BaseAPI):
    """Async Unique API endpoint."""

    async def get(self, field: str, **kwargs: Any) -> dict[str, Any]:
        """Get unique values for a field (async)."""
        params = self._prepare_params(field=field, **kwargs)
        response = await self._client.get("/api/unique", params=params)
        return self._handle_response(response)

    async def multi(self, fields: list[str], **kwargs: Any) -> dict[str, Any]:
        """Get unique values for multiple fields (async)."""
        params = self._prepare_params(fields=",".join(fields), **kwargs)
        response = await self._client.get("/api/multiunique", params=params)
        return self._handle_response(response)

