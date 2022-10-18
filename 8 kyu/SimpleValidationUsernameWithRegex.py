# Simple validation of a username with regex

import re

def validate_usr(username):
    regex = '^[a-z0-9_]{4,16}$'
    
    if re.fullmatch(regex, username):
        return True
    else:
        return False
