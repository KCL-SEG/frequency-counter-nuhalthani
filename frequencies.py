"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = dict()
    tempList = []

    for i in range (len(items)):
        items[i] = str(items[i])

    for i in items:
        frequencies[i] = frequencies.get(i, 0) + 1

    return frequencies
