"""Files API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/files-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI


class FilesAPI(BaseAPI):
    """Files API endpoint."""

    def list(self, **kwargs: Any) -> list[dict[str, Any]]:
        """List files.

        GET - /api/files

        Args:
            **kwargs: Additional parameters

        Returns:
            List of file objects
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get("/api/files", params=params)
        result = self._handle_response(response)
        if isinstance(result, list):
            return result
        return []


class AsyncFilesAPI(BaseAPI):
    """Async Files API endpoint."""

    async def list(self, **kwargs: Any) -> list[dict[str, Any]]:
        """List files (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get("/api/files", params=params)
        result = self._handle_response(response)
        if isinstance(result, list):
            return result
        return []

