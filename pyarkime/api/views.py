"""Views API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/views-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI
from pyarkime.models import ArkimeView


class ViewsAPI(BaseAPI):
    """Views API endpoint."""

    def list(self, **kwargs: Any) -> list[dict[str, Any]]:
        """List all views.

        GET - /api/views

        Args:
            **kwargs: Additional parameters

        Returns:
            List of view objects
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get("/api/views", params=params)
        result = self._handle_response(response)
        if isinstance(result, list):
            return result
        return []

    def create(
        self, view: ArkimeView | dict[str, Any], **kwargs: Any
    ) -> dict[str, Any]:
        """Create a new view.

        POST - /api/view

        Args:
            view: View object or dict
            **kwargs: Additional parameters

        Returns:
            Created view object
        """
        if isinstance(view, ArkimeView):
            view_dict = view.model_dump(exclude_none=True)
        else:
            view_dict = view
        params = self._prepare_params(**view_dict, **kwargs)
        response = self._client.post("/api/view", json=params)
        return self._handle_response(response)

    def get(self, view_id: str, **kwargs: Any) -> dict[str, Any]:
        """Get view by ID.

        GET - /api/view/:id

        Args:
            view_id: View ID
            **kwargs: Additional parameters

        Returns:
            View object
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get(f"/api/view/{view_id}", params=params)
        return self._handle_response(response)

    def update(
        self, view_id: str, view: ArkimeView | dict[str, Any], **kwargs: Any
    ) -> dict[str, Any]:
        """Update a view.

        POST - /api/view/:id

        Args:
            view_id: View ID
            view: View object or dict
            **kwargs: Additional parameters

        Returns:
            Updated view object
        """
        if isinstance(view, ArkimeView):
            view_dict = view.model_dump(exclude_none=True)
        else:
            view_dict = view
        params = self._prepare_params(**view_dict, **kwargs)
        response = self._client.post(f"/api/view/{view_id}", json=params)
        return self._handle_response(response)

    def delete(self, view_id: str, **kwargs: Any) -> dict[str, Any]:
        """Delete a view.

        DELETE - /api/view/:id

        Args:
            view_id: View ID
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.delete(f"/api/view/{view_id}", params=params)
        return self._handle_response(response)


class AsyncViewsAPI(BaseAPI):
    """Async Views API endpoint."""

    async def list(self, **kwargs: Any) -> list[dict[str, Any]]:
        """List all views (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get("/api/views", params=params)
        result = self._handle_response(response)
        if isinstance(result, list):
            return result
        return []

    async def create(
        self, view: ArkimeView | dict[str, Any], **kwargs: Any
    ) -> dict[str, Any]:
        """Create a new view (async)."""
        if isinstance(view, ArkimeView):
            view_dict = view.model_dump(exclude_none=True)
        else:
            view_dict = view
        params = self._prepare_params(**view_dict, **kwargs)
        response = await self._client.post("/api/view", json=params)
        return self._handle_response(response)

    async def get(self, view_id: str, **kwargs: Any) -> dict[str, Any]:
        """Get view by ID (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get(f"/api/view/{view_id}", params=params)
        return self._handle_response(response)

    async def update(
        self, view_id: str, view: ArkimeView | dict[str, Any], **kwargs: Any
    ) -> dict[str, Any]:
        """Update a view (async)."""
        if isinstance(view, ArkimeView):
            view_dict = view.model_dump(exclude_none=True)
        else:
            view_dict = view
        params = self._prepare_params(**view_dict, **kwargs)
        response = await self._client.post(f"/api/view/{view_id}", json=params)
        return self._handle_response(response)

    async def delete(self, view_id: str, **kwargs: Any) -> dict[str, Any]:
        """Delete a view (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.delete(f"/api/view/{view_id}", params=params)
        return self._handle_response(response)

