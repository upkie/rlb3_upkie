#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0

"""Unit tests for the select_env submodule."""

from unittest.mock import patch

from rlb3_upkie.select_env import ENVIRONMENTS, select_env


class TestEnvironments:
    """Test environment constants."""

    def test_environments_list_not_empty(self):
        """Verify ENVIRONMENTS list is not empty."""
        assert len(ENVIRONMENTS) > 0

    def test_environments_are_strings(self):
        """Verify all environment names are strings."""
        assert all(isinstance(env, str) for env in ENVIRONMENTS)

    def test_environments_contain_expected_values(self):
        """Verify expected environment names are present."""
        assert "Upkie-PyBullet-Pendulum" in ENVIRONMENTS


class TestSelectEnv:
    """Test select_env function."""

    @patch("builtins.input", return_value="1")
    def test_select_first_environment(self, mock_input):
        """Test selecting the first environment."""
        result = select_env()
        assert result == ENVIRONMENTS[0]

    @patch("builtins.input", return_value="2")
    def test_select_second_environment(self, mock_input):
        """Test selecting the second environment."""
        result = select_env()
        assert result == ENVIRONMENTS[1]

    @patch("builtins.input", side_effect=["0", "1"])
    def test_invalid_choice_zero_then_valid(self, mock_input):
        """Test invalid choice (0) followed by valid choice."""
        result = select_env()
        assert result == ENVIRONMENTS[0]
        assert mock_input.call_count == 2

    @patch("builtins.input", side_effect=["99", "1"])
    def test_invalid_choice_too_high_then_valid(self, mock_input):
        """Test invalid choice (too high) followed by valid choice."""
        result = select_env()
        assert result == ENVIRONMENTS[0]
        assert mock_input.call_count == 2

    @patch("builtins.input", side_effect=["abc", "1"])
    def test_invalid_choice_non_numeric_then_valid(self, mock_input):
        """Test invalid choice (non-numeric) followed by valid choice."""
        result = select_env()
        assert result == ENVIRONMENTS[0]
        assert mock_input.call_count == 2

    @patch("builtins.input", side_effect=["", "  ", "1"])
    def test_empty_input_then_valid(self, mock_input):
        """Test empty/whitespace input followed by valid choice."""
        result = select_env()
        assert result == ENVIRONMENTS[0]
        assert mock_input.call_count == 3
