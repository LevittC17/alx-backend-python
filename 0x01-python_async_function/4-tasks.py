#!/usr/bin/env python3

'''
Asynchronously spawn task_wait_random `n` times
with the specified `max_delay`
'''


import asyncio
from typing import List

# Import the task_wait_random function from the previous file
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawn task_wait_random 'n' times with the
    specified 'max_delay'.

    Args:
        n (int): The number of times to spawn the task_wait_random
        coroutine.
        max_delay (int): The maximum delay value for each
        task_wait_random call.

    Returns:
        List[float]: A list of delay times (float values) in ascending order.

    This function creates a list of task_wait_random coroutines
    and uses asyncio.gather to execute them concurrently. The resulting
    delays are collected in the 'delays' list and returned.
    """

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    result = await asyncio.gather(*tasks)
    return sorted(result)
