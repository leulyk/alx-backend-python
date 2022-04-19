#!/usr/bin/env python3

"""
    Project: Python - Async Comprehension
    Task 1
"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ Use async comprehension to return a list from a generator """
    return [i async for i in async_generator()]
