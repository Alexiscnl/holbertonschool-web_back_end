#!/usr/bin/env python3
"""
Module for measuring runtime of concurrent coroutines.

This module provides functions for measuring the execution time
of concurrent asynchronous operations and calculating average runtime.
"""
import time
import asyncio
from concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time per coroutine for wait_n.

    Executes wait_n(n, max_delay) and measures the total execution time,
    then returns the average time per coroutine (total_time / n).

    Args:
        n: Number of coroutines to spawn in wait_n
        max_delay: Maximum delay value passed to wait_n

    Returns:
        Average execution time per coroutine as a float

    Example:
        >>> measure_time(5, 9)
        1.759705400466919
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
