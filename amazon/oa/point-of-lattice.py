"""
https://leetcode.com/discuss/interview-question/396418/


"""

import math


def _gcd(x, y):
    if y == 0:
        return x
    return _gcd(y, x % y)


def lattice(ax, ay, bx, by):
    dx = bx - ax
    dy = by - ay

    # rotate 90
    rx, ry = dy, -dx

    # reduce
    gcd = math.abs(_gcd(rx, ry))
    rx /= gcd
    ry /= gcd

    return {bx + rx, by + ry}
