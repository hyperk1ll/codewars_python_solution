# You're a square!

import math

def is_square(n):
    if n < 0:
        return False
    else:
        return n == math.isqrt(n) ** 2
