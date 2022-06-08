# Playing with digits

# Answer 1
def dig_pow(n, p):
    a = str(n)

    total = sum([int(a[i]) ** (p + i) for i in range(len(a))])
    
    if total % n == 0:
        return total / n
    else:
        return -1
      
# Answer 2
def dig_pow(n, p):
    a = 0
    
    for i, c in enumerate(str(n)):
        a += pow(int(c), p + i)
    
    return a / n if a % n == 0 else -1
