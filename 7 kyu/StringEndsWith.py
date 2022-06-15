# String ends with?

def solution(string, ending):
    a = len(ending)
    
    if ending == "":
        return True
    elif string[-a:] == ending:
        return True
    else: 
        return False
