#!/usr/bin/env python3
"""Task 0. Async Generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float]:
    """coroutine called async_generator that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously wait
    1 second, then yield a random number between 0 and 10."""

    asyncio.sleep(1)
    random.uniform(1, 10)
