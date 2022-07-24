def first_non_consecutive(arr):
    a = []
    
    b = arr[0]
    c = arr[-1]
    
    for i in range(b, c + 1):
        a.append(i)
    
    if a == arr:
        return None
    else:
        for i in arr:
            if i in a:
                a.remove(i)
        return a[0] + 1
