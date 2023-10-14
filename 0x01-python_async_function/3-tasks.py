#!/usr/bin/env python3

'''
Create an asyncio.Task for the wait_random coroutine
with the specified max_delay
'''


import asyncio


# Import the wait_random coroutine from the file 0-basic_async_syntax
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''This function creates an asyncio.Task for the wait_random coroutine
    with the specified max_delay and returns the asyncio.Task object
    '''
    return asyncio.create_task(wait_random(max_delay))
