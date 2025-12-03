#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0

"""Unit tests for the wrappers submodule."""

from unittest.mock import Mock, patch

from rlb3_upkie.wrappers import silence_warnings


class TestSilenceWarnings:
    """Test silence_warnings wrapper function."""

    @patch("rlb3_upkie.wrappers.disable_warnings")
    def test_silence_warnings_calls_disable_warnings(self, mock_disable):
        """Verify silence_warnings calls disable_warnings."""
        mock_env = Mock()
        silence_warnings(mock_env)
        mock_disable.assert_called_once()

    @patch("rlb3_upkie.wrappers.disable_warnings")
    def test_silence_warnings_returns_same_env(self, mock_disable):
        """Verify silence_warnings returns the same environment."""
        mock_env = Mock()
        result = silence_warnings(mock_env)
        assert result is mock_env

    @patch("rlb3_upkie.wrappers.disable_warnings")
    def test_silence_warnings_with_none_env(self, mock_disable):
        """Test silence_warnings with None environment."""
        result = silence_warnings(None)
        mock_disable.assert_called_once()
        assert result is None
