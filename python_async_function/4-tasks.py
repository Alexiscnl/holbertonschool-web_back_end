#!/usr/bin/env python3
"""
Module for concurrent coroutines execution with type annotations.

This module provides functions for executing multiple asynchronous coroutines
concurrently and collecting their results in completion order.
"""
import asyncio
from task import task_wait_random


async def task_wait_n(n, max_delay):
    """
    Execute multiple wait_random coroutines concurrently.

    Spawns n instances of wait_random coroutine with the specified max_delay
    and returns a list of all delays in ascending order without using sort().
    The ordering is achieved naturally by collecting results as they complete.

    Args:
        n: Number of wait_random coroutines to spawn
        max_delay: Maximum delay value passed to each wait_random coroutine

    Returns:
        List of float values representing delays in ascending order

    Example:
        >>> asyncio.run(wait_n(5, 5))
        [0.969, 1.026, 1.799, 3.641, 4.500]
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        results.append(delay)
    return results
