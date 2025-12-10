"""Pytest configuration and fixtures."""

import pytest


@pytest.fixture
def base_url() -> str:
    """Base URL for testing."""
    return "https://arkime.example.com"


@pytest.fixture
def username() -> str:
    """Username for testing."""
    return "testuser"


@pytest.fixture
def password() -> str:
    """Password for testing."""
    return "testpass"

