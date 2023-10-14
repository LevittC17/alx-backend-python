#!/usr/bin/env python3

'''
coroutine to loop 10 times, each time asynchronously
wait 1 second then yield a random number between 0
and 10
'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields random numbers between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Wait for 1 second asynchronously
        yield random.uniform(0, 10)
