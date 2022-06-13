# List Filtering

def filter_list(l):
    a = []
    
    for i in l:
        if type(i) == type(1):
            a.append(i)
            
    return a
