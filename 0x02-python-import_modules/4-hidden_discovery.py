#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    """hidden discovery"""
    f = dir(hidden_4)
    for n in f:
        if n[:2] != "__":
            print(n)
