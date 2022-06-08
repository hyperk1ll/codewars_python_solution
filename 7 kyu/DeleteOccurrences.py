# Delete occurrences of an element if it occurs more than n times

def delete_nth(order,max_e):
    a = []
    
    for i in order:
        if a.count(i) < max_e:
            a.append(i)
            
    return a
