#!/usr/bin/env python3
"""Task 2. Run time for four parallel comprehensions"""
import time
import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> List[float]:
    """coroutine that will execute async_comprehension four times
    in parallel using asyncio.gather. measure_runtime should measure
    the total runtime and return it."""
    start_time = time.monotonic()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_runtime = time.monotonic() - start_time

    return total_runtime
