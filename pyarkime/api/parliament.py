"""Parliament API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/parliament-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI


class ParliamentAPI(BaseAPI):
    """Parliament API endpoint."""

    def get(self, **kwargs: Any) -> dict[str, Any]:
        """Get parliament data.

        GET - /api/parliament

        Args:
            **kwargs: Additional parameters

        Returns:
            Parliament data
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get("/api/parliament", params=params)
        return self._handle_response(response)


class AsyncParliamentAPI(BaseAPI):
    """Async Parliament API endpoint."""

    async def get(self, **kwargs: Any) -> dict[str, Any]:
        """Get parliament data (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get("/api/parliament", params=params)
        return self._handle_response(response)

