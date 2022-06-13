# Sort array by string length

# Answer 1
def sort_by_length(arr):
    a = []
    
    for i in arr:
        a.append((len(i), i))
        a.sort()
    
    b = []
    
    for i in a:
        b.append(i[1])
    
    return b

# Answer 2
def sort_by_length(arr):
    return sorted(arr, key=len)
