#!/usr/bin/env python3
"""Returning list of float and integers"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Retrun sum of mxd_lst"""
    return sum(mxd_lst)
