"""Base API class for all API endpoints."""
from __future__ import annotations

from abc import ABC
from typing import Any

import httpx

from pyarkime.exceptions import (
    ArkimeAPIError,
    ArkimeAuthError,
    ArkimeConnectionError,
    ArkimeNotFoundError,
)


class BaseAPI(ABC):
    """Base class for all API endpoint modules.

    Provides common functionality for making HTTP requests,
    handling errors, and parsing responses.
    """

    def __init__(self, client: httpx.Client | httpx.AsyncClient) -> None:
        """Initialize base API.

        Args:
            client: httpx client (sync or async)
        """
        self._client = client

    def _handle_response(self, response: httpx.Response) -> dict[str, Any] | list[Any]:
        """Handle HTTP response and raise appropriate exceptions.

        Args:
            response: HTTP response object

        Returns:
            Parsed JSON response

        Raises:
            ArkimeAuthError: For 401/403 errors (when not API errors)
            ArkimeNotFoundError: For 404 errors
            ArkimeAPIError: For other API errors
            ArkimeConnectionError: For connection errors
        """
        try:
            # Try to parse JSON first to check for success: false
            json_data = None
            try:
                json_data = response.json()
            except ValueError:
                # Not JSON, will handle below
                pass

            # Check if response indicates an error (success: false)
            # This takes precedence over status code
            if isinstance(json_data, dict) and json_data.get("success") is False:
                error_text = json_data.get("text", json_data.get("error", "Unknown error"))
                # Build detailed error message
                error_msg = f"API error: {error_text}"
                # Add additional context if available
                if "ResponseError" in error_text or "parse" in error_text.lower():
                    error_msg += " (This may indicate a query syntax error. Check your expression syntax.)"
                
                # If it's a parse exception or similar, it's an API error, not auth error
                if "parse" in error_text.lower() or "query" in error_text.lower() or "ResponseError" in error_text:
                    raise ArkimeAPIError(
                        error_msg,
                        status_code=response.status_code,
                        response_body=response.text,
                    )
                # Otherwise, check status code for auth errors
                if response.status_code == 401 or response.status_code == 403:
                    raise ArkimeAuthError(
                        f"Authentication failed: {error_text}",
                        status_code=response.status_code,
                        response_body=response.text,
                    )
                else:
                    raise ArkimeAPIError(
                        error_msg,
                        status_code=response.status_code,
                        response_body=response.text,
                    )

            # Handle status codes (only if not already handled above)
            if response.status_code == 401 or response.status_code == 403:
                raise ArkimeAuthError(
                    f"Authentication failed: {response.text}",
                    status_code=response.status_code,
                    response_body=response.text,
                )
            elif response.status_code == 404:
                raise ArkimeNotFoundError(
                    f"Resource not found: {response.text}",
                    status_code=response.status_code,
                    response_body=response.text,
                )
            elif not response.is_success:
                raise ArkimeAPIError(
                    f"API error: {response.text}",
                    status_code=response.status_code,
                    response_body=response.text,
                )

            # Return parsed JSON if available
            if json_data is not None:
                return json_data

            # Try to parse JSON again if we didn't get it the first time
            try:
                return response.json()
            except ValueError as e:
                # Some endpoints return non-JSON (e.g., CSV)
                # Only treat as non-JSON if content-type suggests it's not JSON
                content_type = response.headers.get("content-type", "").lower()
                if "json" in content_type:
                    # Expected JSON but failed to parse - this is an error
                    raise ArkimeAPIError(
                        f"Failed to parse JSON response: {str(e)}",
                        status_code=response.status_code,
                        response_body=response.text,
                    ) from e
                # Non-JSON response (CSV, etc.)
                return {"content": response.text, "content_type": content_type}
        except (ArkimeAuthError, ArkimeNotFoundError, ArkimeAPIError):
            # Re-raise our custom exceptions
            raise
        except httpx.HTTPError as e:
            raise ArkimeConnectionError(f"Connection error: {str(e)}") from e

    def _prepare_params(
        self, params: dict[str, Any] | None = None, **kwargs: Any
    ) -> dict[str, Any]:
        """Prepare query parameters for request.

        Args:
            params: Base parameters dict
            **kwargs: Additional parameters

        Returns:
            Combined parameters dict
        """
        if params is None:
            params = {}
        # Merge kwargs into params, filtering out None values
        for key, value in kwargs.items():
            if value is not None:
                params[key] = value
        return params

