# Fake Binary

def fake_bin(x):
    a = []
    
    for i in x:
        if int(i) >= 5:
            a.append(1)
        elif int(i) < 5:
            a.append(0)
    
    b = [str(int) for int in a]
    res = "".join(b)
    
    return res
