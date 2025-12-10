"""Upload API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/upload-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI


class UploadAPI(BaseAPI):
    """Upload API endpoint."""

    def upload(self, file_path: str, **kwargs: Any) -> dict[str, Any]:
        """Upload a file.

        POST - /api/upload

        Args:
            file_path: Path to file to upload
            **kwargs: Additional parameters

        Returns:
            Upload result
        """
        with open(file_path, "rb") as f:
            files = {"file": f}
            params = self._prepare_params(**kwargs)
            response = self._client.post("/api/upload", files=files, data=params)
        return self._handle_response(response)


class AsyncUploadAPI(BaseAPI):
    """Async Upload API endpoint."""

    async def upload(self, file_path: str, **kwargs: Any) -> dict[str, Any]:
        """Upload a file (async)."""
        with open(file_path, "rb") as f:
            files = {"file": f}
            params = self._prepare_params(**kwargs)
            response = await self._client.post("/api/upload", files=files, data=params)
        return self._handle_response(response)

