# Find the next perfect square!

import math

def find_next_square(sq):
    root = math.sqrt(sq)
    if int(root + 0.5) ** 2 == sq:
        return int(pow(root + 1, 2))
    else:
        return -1
