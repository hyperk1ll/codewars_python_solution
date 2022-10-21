# Moving Zeros To The End

def move_zeros(lst):
    if lst.count(0) == 0:
        return lst
    else:
        for i in lst:
            lst.append(lst.pop(lst.index(0)))
        return lst
    