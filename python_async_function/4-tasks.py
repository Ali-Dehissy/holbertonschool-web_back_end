#!/usr/bin/env python3
"""Module"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Task wait"""
    list_random = []
    for _ in range(n):
        list_random.append(await task_wait_random(max_delay))
    return sorted(list_random)
