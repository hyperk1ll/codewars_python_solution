# Form The Minimum

def min_value(digits):
    a = []
    
    for i in digits:
        if i not in a:
            a.append(i)
            
    a.sort()
    
    x = [str(i) for i in a]
    
    return int(''.join(x))