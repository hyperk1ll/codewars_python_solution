# Duplicate Encoder

def duplicate_encode(word):
    a = []
    
    for i in word.lower():
        if word.lower().count(i) == 1:
            i = '('
            a.append(i)
        elif word.lower().count(i) > 1:
            i = ')'
            a.append(i)
    
    return ''.join(a)
