#!/usr/bin/python3
"""BOXES BOXES"""


def canUnlockAll(boxes):
    """ take boxes """
    total_boxes = len(boxes)
    setofkeys = [0]
    count = 0
    i = 0

    while i < len(setofkeys):
        setkey = setofkeys[i]
        for key in boxes[setkey]:
            if 0 < key < total_boxes and key not in setofkeys:
                setofkeys.append(key)
                count += 1
        i += 1

    return count == total_boxes - 1
