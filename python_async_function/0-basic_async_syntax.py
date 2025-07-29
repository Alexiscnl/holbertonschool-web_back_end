#!/usr/bin/env python3
"""
Module for basic asynchronous operations.

This module provides basic async coroutines for learning async/await syntax
and working with random delays.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds.

    Args:
        max_delay: Maximum delay in seconds (default: 10)

    Returns:
        The actual delay that was waited (float)
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
