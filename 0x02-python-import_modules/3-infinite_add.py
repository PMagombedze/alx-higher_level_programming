#!/usr/bin/python3
import sys
if __name__ == "__main__":
    """infinite add"""
    c = len(sys.argv)
    count = 0
    for n in range(1, c):
        count += int(sys.argv[n])
    print(count)
