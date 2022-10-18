# Regexp Basics - is it a digit?

import re

def is_digit(n):
    regex = '^[0-9]$'
    
    if re.fullmatch(regex, n):
        return True
    else:
        return False