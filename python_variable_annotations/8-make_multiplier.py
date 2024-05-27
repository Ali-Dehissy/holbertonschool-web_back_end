#!/usr/bin/env python3
"""
Complex types Functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Multiplication
    """
    def function(var: float):
        """
        Complex types Functions
        """
        return var * multiplier
    return function
