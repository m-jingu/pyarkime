"""Shortcuts API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/shortcuts-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI
from pyarkime.models import Shortcut


class ShortcutsAPI(BaseAPI):
    """Shortcuts API endpoint."""

    def list(self, **kwargs: Any) -> list[dict[str, Any]]:
        """List all shortcuts.

        GET - /api/shortcuts

        Args:
            **kwargs: Additional parameters

        Returns:
            List of shortcut objects
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get("/api/shortcuts", params=params)
        result = self._handle_response(response)
        if isinstance(result, list):
            return result
        return []

    def create(
        self, shortcut: Shortcut | dict[str, Any], **kwargs: Any
    ) -> dict[str, Any]:
        """Create a new shortcut.

        POST - /api/shortcut

        Args:
            shortcut: Shortcut object or dict
            **kwargs: Additional parameters

        Returns:
            Created shortcut object
        """
        if isinstance(shortcut, Shortcut):
            shortcut_dict = shortcut.model_dump(exclude_none=True)
        else:
            shortcut_dict = shortcut
        params = self._prepare_params(**shortcut_dict, **kwargs)
        response = self._client.post("/api/shortcut", json=params)
        return self._handle_response(response)

    def get(self, shortcut_id: str, **kwargs: Any) -> dict[str, Any]:
        """Get shortcut by ID.

        GET - /api/shortcut/:id

        Args:
            shortcut_id: Shortcut ID
            **kwargs: Additional parameters

        Returns:
            Shortcut object
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get(f"/api/shortcut/{shortcut_id}", params=params)
        return self._handle_response(response)

    def update(
        self, shortcut_id: str, shortcut: Shortcut | dict[str, Any], **kwargs: Any
    ) -> dict[str, Any]:
        """Update a shortcut.

        POST - /api/shortcut/:id

        Args:
            shortcut_id: Shortcut ID
            shortcut: Shortcut object or dict
            **kwargs: Additional parameters

        Returns:
            Updated shortcut object
        """
        if isinstance(shortcut, Shortcut):
            shortcut_dict = shortcut.model_dump(exclude_none=True)
        else:
            shortcut_dict = shortcut
        params = self._prepare_params(**shortcut_dict, **kwargs)
        response = self._client.post(f"/api/shortcut/{shortcut_id}", json=params)
        return self._handle_response(response)

    def delete(self, shortcut_id: str, **kwargs: Any) -> dict[str, Any]:
        """Delete a shortcut.

        DELETE - /api/shortcut/:id

        Args:
            shortcut_id: Shortcut ID
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.delete(f"/api/shortcut/{shortcut_id}", params=params)
        return self._handle_response(response)


class AsyncShortcutsAPI(BaseAPI):
    """Async Shortcuts API endpoint."""

    async def list(self, **kwargs: Any) -> list[dict[str, Any]]:
        """List all shortcuts (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get("/api/shortcuts", params=params)
        result = self._handle_response(response)
        if isinstance(result, list):
            return result
        return []

    async def create(
        self, shortcut: Shortcut | dict[str, Any], **kwargs: Any
    ) -> dict[str, Any]:
        """Create a new shortcut (async)."""
        if isinstance(shortcut, Shortcut):
            shortcut_dict = shortcut.model_dump(exclude_none=True)
        else:
            shortcut_dict = shortcut
        params = self._prepare_params(**shortcut_dict, **kwargs)
        response = await self._client.post("/api/shortcut", json=params)
        return self._handle_response(response)

    async def get(self, shortcut_id: str, **kwargs: Any) -> dict[str, Any]:
        """Get shortcut by ID (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get(f"/api/shortcut/{shortcut_id}", params=params)
        return self._handle_response(response)

    async def update(
        self, shortcut_id: str, shortcut: Shortcut | dict[str, Any], **kwargs: Any
    ) -> dict[str, Any]:
        """Update a shortcut (async)."""
        if isinstance(shortcut, Shortcut):
            shortcut_dict = shortcut.model_dump(exclude_none=True)
        else:
            shortcut_dict = shortcut
        params = self._prepare_params(**shortcut_dict, **kwargs)
        response = await self._client.post(f"/api/shortcut/{shortcut_id}", json=params)
        return self._handle_response(response)

    async def delete(self, shortcut_id: str, **kwargs: Any) -> dict[str, Any]:
        """Delete a shortcut (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.delete(f"/api/shortcut/{shortcut_id}", params=params)
        return self._handle_response(response)

