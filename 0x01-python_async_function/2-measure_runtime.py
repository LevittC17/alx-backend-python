#!/usr/bin/env python3

'''
measure the runtime...
`time` module to measure an approximate elapsed time
'''


import asyncio
import time


# Import the wait_n function from the previous file
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Measure the total execution time for wait_n(n, max_delay) and
    return total_time / n
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    average_time = total_time / n

    return average_time
