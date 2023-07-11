#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """pascal"""
    if n <= 0:
        return []
    pasc = [[1]]
    while len(pasc) != n:
        sh = pasc[-1]
        ch = [1]
        for a in range(len(sh) - 1):
            ch.append(sh[a] + sh[a + 1])
        ch.append(1)
        pasc.append(ch)
    return pasc
