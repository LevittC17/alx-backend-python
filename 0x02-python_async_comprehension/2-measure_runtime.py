#!/usr/bin/env python3

'''
Run time for four parallel comprehensions
'''


import asyncio
from typing import List
from time import time


# Import the async_comprehension coroutine from the previous task
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measure the total runtime of executing async_comprehension
    four times in parallel using asyncio.gather'''
    start_time = time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time()
    total_runtime = end_time - start_time

    return total_runtime
