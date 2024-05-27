#!/usr/bin/env python3
"""
Complex types - String and int
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return Tuple
    """
    return (k, v**2)
