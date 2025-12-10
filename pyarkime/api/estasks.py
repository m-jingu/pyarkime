"""ESTasks API endpoint.
from __future__ import annotations

See: https://arkime.com/apiv3#/estasks-API
"""

from typing import Any

from pyarkime.api.base import BaseAPI


class ESTasksAPI(BaseAPI):
    """Elasticsearch tasks API endpoint."""

    def list(self, **kwargs: Any) -> list[dict[str, Any]]:
        """List Elasticsearch tasks.

        GET - /api/estasks

        Args:
            **kwargs: Additional parameters

        Returns:
            List of task objects
        """
        params = self._prepare_params(**kwargs)
        response = self._client.get("/api/estasks", params=params)
        result = self._handle_response(response)
        if isinstance(result, list):
            return result
        return []

    def cancel(self, task_id: str, **kwargs: Any) -> dict[str, Any]:
        """Cancel a task.

        POST - /api/estasks/:id/cancel

        Args:
            task_id: Task ID
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.post(f"/api/estasks/{task_id}/cancel", json=params)
        return self._handle_response(response)

    def cancel_with(self, task_id: str, **kwargs: Any) -> dict[str, Any]:
        """Cancel a task with parameters.

        POST - /api/estasks/:id/cancelwith

        Args:
            task_id: Task ID
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.post(f"/api/estasks/{task_id}/cancelwith", json=params)
        return self._handle_response(response)

    def cancel_all(self, **kwargs: Any) -> dict[str, Any]:
        """Cancel all tasks.

        POST - /api/estasks/cancelall

        Args:
            **kwargs: Additional parameters

        Returns:
            Operation result
        """
        params = self._prepare_params(**kwargs)
        response = self._client.post("/api/estasks/cancelall", json=params)
        return self._handle_response(response)


class AsyncESTasksAPI(BaseAPI):
    """Async ESTasks API endpoint."""

    async def list(self, **kwargs: Any) -> list[dict[str, Any]]:
        """List Elasticsearch tasks (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.get("/api/estasks", params=params)
        result = self._handle_response(response)
        if isinstance(result, list):
            return result
        return []

    async def cancel(self, task_id: str, **kwargs: Any) -> dict[str, Any]:
        """Cancel a task (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.post(f"/api/estasks/{task_id}/cancel", json=params)
        return self._handle_response(response)

    async def cancel_with(self, task_id: str, **kwargs: Any) -> dict[str, Any]:
        """Cancel a task with parameters (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.post(f"/api/estasks/{task_id}/cancelwith", json=params)
        return self._handle_response(response)

    async def cancel_all(self, **kwargs: Any) -> dict[str, Any]:
        """Cancel all tasks (async)."""
        params = self._prepare_params(**kwargs)
        response = await self._client.post("/api/estasks/cancelall", json=params)
        return self._handle_response(response)

