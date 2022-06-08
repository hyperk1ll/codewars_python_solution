# Correct the mistakes of the character recognition software

def correct(s):
    a = [i for i in s]
    
    for n in range(0,len(a)):
        if a[n] == '5': a[n] = 'S'
        if a[n] == '0': a[n] = 'O'
        if a[n] == '1': a[n] = 'I'
    
    return ''.join(a)
