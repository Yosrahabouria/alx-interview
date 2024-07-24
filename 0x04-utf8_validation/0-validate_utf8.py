#!/usr/bin/python3
"""
Validate utf-8
"""


def validUTF8(data):
    count = 0
    first_bit = 1 << 7
    second_bit = 1 << 6

    for num in data:
        current_bit = 1 << 7

        if count == 0:
            while current_bit & num:
                count += 1
                current_bit >>= 1

            if count == 0:
                continue

            if count == 1 or count > 4:
                return False

        else:
            if not (num & first_bit and not (num & second_bit)):
                return False

        count -= 1

    return count == 0
