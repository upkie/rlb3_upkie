#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 Inria

"""Environment wrapper to silence Upkie warnings in subprocess environments."""

import logging

import gymnasium as gym
from upkie.logging import disable_warnings


class SuppressUpkieWarnings(logging.Filter):
    """Filter that suppresses Upkie warning messages."""

    def filter(self, record):
        if ( record.name == "loop_rate_limiters" and record.levelno == logging.WARNING):
            return False
        return True


def silence_warnings(env: gym.Env) -> gym.Env:
    """
    Wrapper function to silence Upkie warnings in subprocess environments.

    This is called in each subprocess when using SubprocVecEnv, ensuring
    that warnings are suppressed in all parallel environments.

    Args:
        env: The environment to wrap

    Returns:
        The same environment (warnings are suppressed globally per process)
    """
    # Suppress warnings in this subprocess
    disable_warnings()

    # Add a filter to the root logger to catch any warnings that slip through
    warning_suppressor = SuppressUpkieWarnings()
    logging.getLogger().addFilter(warning_suppressor)
    logging.getLogger("loop_rate_limiters").addFilter(warning_suppressor)
    logging.getLogger("loop_rate_limiters").setLevel(logging.ERROR)

    return env
