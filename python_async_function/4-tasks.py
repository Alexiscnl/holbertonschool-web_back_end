#!/usr/bin/env python3
"""
Module for executing multiple asynchronous waits and returning sorted delays.

Functions:
    wait_n(n: int, max_delay: int) -> list[float]:
    Spawns n wait_random coroutines & returns their delays in ascending order.
"""
from typing import List
import asyncio
import importlib

task_wait_random = importlib.import_module("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple coroutines concurrently and return sorted delays
    """
    delays_coroutines = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*delays_coroutines)
    return sorted(delays)
