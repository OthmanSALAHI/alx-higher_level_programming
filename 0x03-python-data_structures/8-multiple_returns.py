#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if not sentence:
        firstLetter = None
    else:
        firstLetter = sentence[0]
    return length, firstLetter
