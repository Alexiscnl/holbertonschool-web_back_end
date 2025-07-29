#!/usr/bin/env python3
"""
Module for asynchronous generators.

This module provides async generators that yield random values
with asynchronous delays between generations.
"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields 10 random floats.

    Loops 10 times, each time asynchronously waits 1 second,
    then yields a random number between 0 and 10.

    Yields:
        float: Random number between 0 and 10

    Example:
        >>> async for value in async_generator():
        ...     print(value)
        4.403136952967102
        6.9092712604587465
        ...
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
