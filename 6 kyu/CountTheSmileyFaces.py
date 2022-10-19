# Count the smiley faces!

import re

def count_smileys(arr):
    return sum(1 for i in arr if re.match(r'[:;][-~]?[)D]', i))