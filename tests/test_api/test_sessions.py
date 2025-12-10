"""Tests for sessions API."""

import pytest

from pyarkime import ArkimeClient, AsyncArkimeClient


def test_sessions_api_access(base_url: str, username: str, password: str) -> None:
    """Test sessions API access."""
    client = ArkimeClient(base_url, username, password)
    assert client.sessions is not None
    client.close()


@pytest.mark.asyncio
async def test_async_sessions_api_access(
    base_url: str, username: str, password: str
) -> None:
    """Test async sessions API access."""
    client = AsyncArkimeClient(base_url, username, password)
    assert client.sessions is not None
    await client.close()

