#!/usr/bin/env python3
"""
Module for measuring runtime of parallel async comprehensions.

This module provides functions to measure execution time when running
multiple async comprehensions in parallel using asyncio.gather.
"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of four parallel async comprehensions.

    Executes four instances of async_comprehension concurrently using
    asyncio.gather and measures the total execution time. The runtime
    should be approximately 10 seconds since all comprehensions run
    in parallel rather than sequentially.

    Returns:
        float: Total execution time in seconds

    Example:
        >>> import asyncio
        >>> runtime = asyncio.run(measure_runtime())
        >>> 9.0 < runtime < 12.0  # Should be around 10 seconds
        True
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time
