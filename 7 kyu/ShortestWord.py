# Shortest Word

def find_short(s):
    words = s.split() 
    
    a = []
    for i in words:
        a.append(len(i))
        
    a.sort()
    
    return a[0]
