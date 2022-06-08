# Descending Order

def descending_order(num):
    a = [int(x) for x in str(num)]
    a.sort(reverse = True)
    
    res = int("".join(map(str, a)))
    return res
