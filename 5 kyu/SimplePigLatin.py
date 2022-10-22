# Simple Pig Latin

def pig_it(text):
    a = text.split(" ")
    
    x = []
    
    for i in a:
        if i.isalpha():
            x.append(i[1:]+i[0]+'ay')
        else:
            x.append(i)

    return " ".join(x)