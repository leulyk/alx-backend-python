#!/usr/bin/env python3

"""
    Project: Python - Async
    Task 1
"""

from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        Executes a coroutine that waits for random delays
        and returns a list of the waited times in
        ascending order
    """
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
