#!/usr/bin/env python3
"""Async"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collecting 10 random numbs"""
    list_comp = [i async for i in async_generator()]
    return list_comp
