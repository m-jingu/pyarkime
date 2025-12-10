"""Tests for client classes."""

import pytest

from pyarkime import ArkimeClient, AsyncArkimeClient


def test_client_initialization(base_url: str, username: str, password: str) -> None:
    """Test client initialization."""
    client = ArkimeClient(base_url, username, password)
    assert client.base_url == base_url
    assert client.username == username
    assert client.password == password
    client.close()


def test_client_context_manager(base_url: str, username: str, password: str) -> None:
    """Test client context manager."""
    with ArkimeClient(base_url, username, password) as client:
        assert client.base_url == base_url


@pytest.mark.asyncio
async def test_async_client_initialization(
    base_url: str, username: str, password: str
) -> None:
    """Test async client initialization."""
    client = AsyncArkimeClient(base_url, username, password)
    assert client.base_url == base_url
    assert client.username == username
    assert client.password == password
    await client.close()


@pytest.mark.asyncio
async def test_async_client_context_manager(
    base_url: str, username: str, password: str
) -> None:
    """Test async client context manager."""
    async with AsyncArkimeClient(base_url, username, password) as client:
        assert client.base_url == base_url

