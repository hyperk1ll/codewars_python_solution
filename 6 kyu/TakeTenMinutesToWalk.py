# Take a Ten Minutes Walk

def is_valid_walk(walk):
    a = []
    b = []
    
    count = 0
    
    for i in walk:
        if count % 2 == 1:
            a.append(i)
        count += 1
    
    for i in walk:
        if count % 2 == 0:
            b.append(i)
        count += 1
    
    if len(walk) < 10:
        return False
    else:
        if len(set(a)) == 1 and len(set(b)) == 1:
            return True
        else:
            return False


def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    else:
        if walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e'):
            return True
        else:
            return False