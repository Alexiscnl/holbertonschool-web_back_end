#!/usr/bin/env python3
"""
Module for concurrent coroutines execution.

This module provides functions for executing multiple asynchronous coroutines
concurrently and collecting their results in completion order.
"""
import asyncio
from basic_async_syntax import wait_random


# ⚠️ Annotations manquantes
async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Execute multiple wait_random coroutines concurrently.

    Spawns n instances of wait_random coroutine with the specified max_delay
    and returns a list of all delays in ascending order without using sort().

    Args:
        n: Number of wait_random coroutines to spawn
        max_delay: Maximum delay value passed to each wait_random coroutine

    Returns:
        List of float values representing delays in ascending order
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        results.append(delay)
    return results
