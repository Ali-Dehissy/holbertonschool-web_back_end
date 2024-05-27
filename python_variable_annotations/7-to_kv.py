#!/usr/bin/env python3
"""Complex types"""  
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns Tuple"""
    return (k, v**2)
