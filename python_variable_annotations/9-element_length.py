#!/usr/bin/env python3
"""
Iterable object
"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns values with the appropriate type
    """
    return [(i, len(i)) for i in lst]
