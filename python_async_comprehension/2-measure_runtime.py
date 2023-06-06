#!/usr/bin/env python3
"""Async measure time"""
import time
import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executing async comprehension
    measure time"""
    time1 = time.time()
    await asyncio.gather(async_comprehension())
    time2 = time.time()
    total_t = time2 - time1
    return total_t
