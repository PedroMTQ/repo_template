"""Shared pytest fixtures and configuration for repo_template tests."""

from unittest.mock import MagicMock

import pytest


@pytest.fixture
def mock_logger() -> MagicMock:
    """Provide a mock logger for tests that need to assert on log calls without side effects."""
    return MagicMock()
