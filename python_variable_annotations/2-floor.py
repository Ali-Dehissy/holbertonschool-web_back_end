#!/usr/bin/env python3
"""Function which takes a float n as argument and returns the floor of the float"""


def floor(n: float) -> int:
    """Returning largest int value less than or equal to n"""
    return int(n) if n >= 0 else int(n) - 1
