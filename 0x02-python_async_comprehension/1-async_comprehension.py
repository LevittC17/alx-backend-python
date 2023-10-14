#!/usr/bin/env python3

'''
Async Comprehensions
'''


import asyncio
from typing import List


# Import the async_generator coroutine from the task 0-async_generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Collect 10 random numbers using an asynchronous
    comprehension over async_generator'''
    return [number async for number in async_generator()]
