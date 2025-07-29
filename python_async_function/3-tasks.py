#!/usr/bin/env python3
"""
Module for creating asyncio Tasks from coroutines.

This module provides functions for wrapping coroutines into asyncio.Task objects
for better task management and scheduling in asynchronous programs.
"""
import asyncio
from basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task[float]:
    """
    Create an asyncio.Task from the wait_random coroutine.

    Takes a max_delay parameter and wraps the wait_random coroutine
    into an asyncio.Task object that can be scheduled and managed
    by the event loop.

    Args:
        max_delay: Maximum delay value passed to wait_random coroutine

    Returns:
        An asyncio.Task object wrapping the wait_random coroutine

    Example:
        >>> task = task_wait_random(5)
        >>> print(task.__class__)
        <class '_asyncio.Task'>
    """
    return asyncio.create_task(wait_random(max_delay))
