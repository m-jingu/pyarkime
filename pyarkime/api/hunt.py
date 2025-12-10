"""Hunt API endpoint.

See: https://arkime.com/apiv3#/hunt-API
"""
from __future__ import annotations

from typing import Any

from pyarkime.api.base import BaseAPI
from pyarkime.models import Hunt


class HuntAPI(BaseAPI):
    """Hunt (packet search job) API endpoint."""

    def create(
        self,
        name: str,
        query: str,
        size: int,
        search_type: str | None = None,
        notifier: str | None = None,
        users: list[str] | None = None,
        roles: list[str] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create a new hunt.

        POST - /api/hunt

        Args:
            name: Hunt name
            query: Search query
            size: Number of packets to search
            search_type: Search type
            notifier: Notifier name
            users: List of user IDs
            roles: List of role names
            **kwargs: Additional parameters

        Returns:
            Created hunt object
        """
        params = self._prepare_params(
            name=name,
            query=query,
            size=size,
            searchType=search_type,
            notifier=notifier,
            users=users,
            roles=roles,
            **kwargs,
        )
        response = self._client.post("/api/hunt", json=params)
        return self._handle_response(response)

    def list(self, **kwargs: Any) -> list[dict[str, Any]]:
        """List all hunts.

        GET - /api/hunts

        Args:
            **kwargs: Additional parameters

        Returns:
            List of hunt objects
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get("/api/hunts", params=params)
        result = self._handle_response(response)
        if isinstance(result, list):
            return result
        return []

    def get(self, hunt_id: str, **kwargs: Any) -> dict[str, Any]:
        """Get hunt by ID.

        GET - /api/hunt/:id

        Args:
            hunt_id: Hunt ID
            **kwargs: Additional parameters

        Returns:
            Hunt object
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get(f"/api/hunt/{hunt_id}", params=params)
        return self._handle_response(response)

    def cancel(self, hunt_id: str, **kwargs: Any) -> dict[str, Any]:
        """Cancel a hunt.

        POST - /api/hunt/:id/cancel

        Args:
            hunt_id: Hunt ID
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.post(f"/api/hunt/{hunt_id}/cancel", json=params)
        return self._handle_response(response)

    def pause(self, hunt_id: str, **kwargs: Any) -> dict[str, Any]:
        """Pause a hunt.

        POST - /api/hunt/:id/pause

        Args:
            hunt_id: Hunt ID
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.post(f"/api/hunt/{hunt_id}/pause", json=params)
        return self._handle_response(response)

    def play(self, hunt_id: str, **kwargs: Any) -> dict[str, Any]:
        """Resume a paused hunt.

        POST - /api/hunt/:id/play

        Args:
            hunt_id: Hunt ID
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.post(f"/api/hunt/{hunt_id}/play", json=params)
        return self._handle_response(response)

    def remove_from_sessions(
        self, hunt_id: str, session_ids: list[str], **kwargs: Any
    ) -> dict[str, Any]:
        """Remove sessions from a hunt.

        POST - /api/hunt/:id/removefromsessions

        Args:
            hunt_id: Hunt ID
            session_ids: List of session IDs to remove
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(ids=session_ids, **kwargs)
        response = self._client.post(
            f"/api/hunt/{hunt_id}/removefromsessions", json=params
        )
        return self._handle_response(response)

    def update(
        self, hunt_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Update a hunt.

        POST - /api/hunt/:id

        Args:
            hunt_id: Hunt ID
            **kwargs: Hunt fields to update

        Returns:
            Updated hunt object
        """
        params = self._prepare_params(**kwargs)
        response = self._client.post(f"/api/hunt/{hunt_id}", json=params)
        return self._handle_response(response)

    def get_users(self, hunt_id: str, **kwargs: Any) -> list[dict[str, Any]]:
        """Get users for a hunt.

        GET - /api/hunt/:id/users

        Args:
            hunt_id: Hunt ID
            **kwargs: Additional parameters

        Returns:
            List of user objects
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get(f"/api/hunt/{hunt_id}/users", params=params)
        result = self._handle_response(response)
        if isinstance(result, list):
            return result
        return []

    def get_user(
        self, hunt_id: str, user_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Get user for a hunt.

        GET - /api/hunt/:id/user/:user

        Args:
            hunt_id: Hunt ID
            user_id: User ID
            **kwargs: Additional parameters

        Returns:
            User object
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get(
            f"/api/hunt/{hunt_id}/user/{user_id}", params=params
        )
        return self._handle_response(response)


class AsyncHuntAPI(BaseAPI):
    """Async Hunt API endpoint."""

    async def create(
        self,
        name: str,
        query: str,
        size: int,
        search_type: str | None = None,
        notifier: str | None = None,
        users: list[str] | None = None,
        roles: list[str] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create a new hunt (async)."""
        params = self._prepare_params(
            name=name,
            query=query,
            size=size,
            searchType=search_type,
            notifier=notifier,
            users=users,
            roles=roles,
            **kwargs,
        )
        response = await self._client.post("/api/hunt", json=params)
        return self._handle_response(response)

    async def list(self, **kwargs: Any) -> list[dict[str, Any]]:
        """List all hunts (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get("/api/hunts", params=params)
        result = self._handle_response(response)
        if isinstance(result, list):
            return result
        return []

    async def get(self, hunt_id: str, **kwargs: Any) -> dict[str, Any]:
        """Get hunt by ID (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get(f"/api/hunt/{hunt_id}", params=params)
        return self._handle_response(response)

    async def cancel(self, hunt_id: str, **kwargs: Any) -> dict[str, Any]:
        """Cancel a hunt (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.post(f"/api/hunt/{hunt_id}/cancel", json=params)
        return self._handle_response(response)

    async def pause(self, hunt_id: str, **kwargs: Any) -> dict[str, Any]:
        """Pause a hunt (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.post(f"/api/hunt/{hunt_id}/pause", json=params)
        return self._handle_response(response)

    async def play(self, hunt_id: str, **kwargs: Any) -> dict[str, Any]:
        """Resume a paused hunt (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.post(f"/api/hunt/{hunt_id}/play", json=params)
        return self._handle_response(response)

    async def remove_from_sessions(
        self, hunt_id: str, session_ids: list[str], **kwargs: Any
    ) -> dict[str, Any]:
        """Remove sessions from a hunt (async)."""
        params = self._prepare_params(ids=session_ids, **kwargs)
        response = await self._client.post(
            f"/api/hunt/{hunt_id}/removefromsessions", json=params
        )
        return self._handle_response(response)

    async def update(self, hunt_id: str, **kwargs: Any) -> dict[str, Any]:
        """Update a hunt (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.post(f"/api/hunt/{hunt_id}", json=params)
        return self._handle_response(response)

    async def get_users(self, hunt_id: str, **kwargs: Any) -> list[dict[str, Any]]:
        """Get users for a hunt (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get(f"/api/hunt/{hunt_id}/users", params=params)
        result = self._handle_response(response)
        if isinstance(result, list):
            return result
        return []

    async def get_user(
        self, hunt_id: str, user_id: str, **kwargs: Any
    ) -> dict[str, Any]:
        """Get user for a hunt (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get(
            f"/api/hunt/{hunt_id}/user/{user_id}", params=params
        )
        return self._handle_response(response)

