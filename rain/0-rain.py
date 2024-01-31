#!/usr/bin/python3
""" calculate the rain"""


def rain(walls):
    if not walls or len(walls) < 3:
        return 0

    total_water = 0

    for i in range(1, len(walls) - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])
        right = walls[i]
        for j in range(i + 1, len(walls)):
            right = max(right, walls[j])
        total_water += min(left, right) - walls[i]
    return total_water
