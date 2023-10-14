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
    """Measure the total runtime of executing
    async_comprehension four times in parallel."""
    start_time = time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time()
    total_runtime = end_time - start_time
    return total_runtime
