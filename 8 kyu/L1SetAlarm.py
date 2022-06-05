# L1: Set Alarm

# Answer 1
def set_alarm(employed, vacation):
    return employed and not vacation
  
# Answer 2
def set_alarm(employed, vacation):
    if(employed == True and vacation == True):
        return False
    elif (employed == False and vacation == True):
        return False
    elif (employed == False and vacation == False):
        return False
    elif (employed == True and vacation == False):
        return True
