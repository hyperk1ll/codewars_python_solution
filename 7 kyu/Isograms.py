# Isograms

def is_isogram(string):
    a = [x.lower() for x in string]
    
    for x in a:
        if a.count(x) > 1:
            return False
    return True
