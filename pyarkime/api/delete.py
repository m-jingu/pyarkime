"""Delete API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/delete-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI


class DeleteAPI(BaseAPI):
    """Delete API endpoint."""

    def delete_sessions(
        self, ids: list[str], **kwargs: Any
    ) -> dict[str, Any]:
        """Delete sessions.

        POST - /api/delete

        Args:
            ids: List of session IDs (format: "nodeName:sessionId")
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(ids=ids, **kwargs)
        response = self._client.post("/api/delete", json=params)
        return self._handle_response(response)


class AsyncDeleteAPI(BaseAPI):
    """Async Delete API endpoint."""

    async def delete_sessions(
        self, ids: list[str], **kwargs: Any
    ) -> dict[str, Any]:
        """Delete sessions (async)."""
        params = self._prepare_params(ids=ids, **kwargs)
        response = await self._client.post("/api/delete", json=params)
        return self._handle_response(response)

