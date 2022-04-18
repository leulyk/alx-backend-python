#!/usr/bin/env python3

"""
    Project: Python - Async
    Task 0
"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
        A coroutine that waits for a random delay
        and returns the delay time in seconds
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
