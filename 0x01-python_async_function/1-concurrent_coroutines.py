#!/usr/bin/env python3

'''
Asynchronously spawn the wait_random caroutine `n`
times with the specified `max_delay`
'''


import asyncio
from typing import List

# import the wait_random caroutine from the file 0-basic_async_syntax.py
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''This function creates a list of wait_random caroutines and uses
    asyncio.as_completed to ensure the results are obtained in ascending order.
    The resulting delays are collected in the 'delays' list and returned
    '''
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
