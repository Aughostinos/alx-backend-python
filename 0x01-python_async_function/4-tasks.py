#!/usr/bin/env python3
"""Task 4: Altering wait_n into task_wait_n"""

import asyncio
import heapq
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    The code is nearly identical to wait_n except task_wait_random
    is being called.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    heapq.heapify(delays)
    return [heapq.heappop(delays) for _ in range(len(delays))]
