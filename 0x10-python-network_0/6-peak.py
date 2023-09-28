#!/usr/bin/python3
"""peak."""


def find_peak(list_of_integers):
    """peak in a list of unsorted integers."""
    if list_of_integers:
        d_ = sorted(list_of_integers)
        c_ = d_[: : -1]
        return c_[0]
