"""Tests for repo_template.core.my_service."""

from unittest.mock import patch

import pytest

from repo_template.core.my_service import my_mock_function


def test_my_mock_function_accepts_args_and_kwargs() -> None:
    """Calling my_mock_function with positional and keyword arguments does not raise."""
    my_mock_function('a', 'b', key='value')


def test_my_mock_function_logs_message_with_args_and_kwargs(mock_logger: object) -> None:
    """my_mock_function calls logger.info with a message containing the given args and kwargs."""
    with patch('repo_template.core.my_service.logger', mock_logger):
        my_mock_function('hello', world='!')
    mock_logger.info.assert_called_once()
    (message,) = mock_logger.info.call_args[0]
    assert 'hello' in message
    assert 'world' in message
    assert '!' in message
