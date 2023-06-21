#!/usr/bin/env python3
"""Helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns Tuple"""
    end: int = page * page_size
    start: int = 0
    for x in range(page - 1):
        start += page_size
    return (start, end)
