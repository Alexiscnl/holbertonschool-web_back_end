#!/usr/bin/env python3
import asyncio
import random

async def wait_random(max_delay = 10):
    """
    Waits for a random delay between 0 and max_delay seconds and returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
