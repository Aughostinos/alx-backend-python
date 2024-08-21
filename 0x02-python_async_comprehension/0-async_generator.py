#!/usr/bin/env python3
"""Task 0. Async Generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float]:
    asyncio.sleep(1)
    random.uniform(1, 10)