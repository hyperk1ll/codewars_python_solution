# Count the Digit

def nb_dig(n, d):
    count = 0
    s = str(d)
    
    for i in range(n + 1):
        num = pow(i, 2)
        count += str(num).count(s)

    return count
