#!/usr/bin/env python3
"""
Module for async comprehensions.

This module provides functions that use async comprehensions to collect
values from asynchronous generators efficiently.
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehension.

    Uses an async comprehension to iterate over async_generator and collect
    all the yielded random numbers into a list.

    Returns:
        List[float]: A list containing 10 random numbers between 0 and 10

    Example:
        >>> result = await async_comprehension()
        >>> len(result)
        10
        >>> all(0 <= num <= 10 for num in result)
        True
    """
    return [value async for value in async_generator()]
