"""Digest authentication for Arkime API."""

from typing import TYPE_CHECKING

import httpx

if TYPE_CHECKING:
    from httpx import Auth, Request, Response


class DigestAuth:
    """Digest authentication handler for httpx.

    Arkime uses digest authentication for all API calls.
    This class implements the digest authentication protocol.
    """

    def __init__(self, username: str, password: str) -> None:
        """Initialize digest authentication.

        Args:
            username: Username for authentication
            password: Password for authentication
        """
        self.username = username
        self.password = password

    def __call__(self, request: "Request") -> "Request":
        """Add authentication to request.

        Note: httpx has built-in digest auth support via httpx.DigestAuth.
        This is a placeholder that will be replaced with httpx.DigestAuth
        in the client implementation.

        Args:
            request: HTTP request to authenticate

        Returns:
            Authenticated request
        """
        # This method is not actually used.
        # We use httpx.DigestAuth directly in the client.
        return request


def create_auth(username: str, password: str) -> "Auth":
    """Create httpx digest auth instance.

    Args:
        username: Username for authentication
        password: Password for authentication

    Returns:
        httpx.DigestAuth instance
    """
    return httpx.DigestAuth(username, password)

