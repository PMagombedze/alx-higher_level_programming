#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    """hidden discovery"""
    f = dir(hidden_4)
    for n in f:
        if n[:2] != "__":
            print(n)
