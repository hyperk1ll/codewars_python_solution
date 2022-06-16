# Two to One

def longest(a1, a2):
    a = list(set(a1+a2))
    a.sort()
    return ''.join(a)
