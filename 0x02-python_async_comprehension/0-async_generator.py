#!/usr/bin/env python3

"""
    Project: Python - Async comprehension
    Task 0
"""

import asyncio
from random import uniform
from typing import Generator


async def async_generator():
    """
        A coroutine that generates a random number between
        0 and 10
    """
    for i in range(10):
        delay = uniform(0, 10)
        await asyncio.sleep(delay)
        yield delay
