#!/usr/bin/python3
def multiple_returns(sentence):
    n = len(sentence)
    if n == 0:
        j = n, None
        return j
    j = n, sentence[0]
    return j
