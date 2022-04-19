#!/usr/bin/env python3

"""
    Project: Python - Async comprehension
    Task 2
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measures the runtime of 4 async comprehensions """
    start = time.time()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    end = time.time()
    return end - start
