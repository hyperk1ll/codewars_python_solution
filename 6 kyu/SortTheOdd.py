# Sort the odd

def sort_array(source_array):
    odd = sorted([x for x in source_array if  x % 2 != 0])
    a = -1
    
    arr = []
    
    for i in source_array:
        a = a + 1
        if i % 2 != 0 :
            arr.append(a)
    
    for x in range (len(arr)):
        z = arr[x]
        source_array[z] = odd[x]
    
    return source_array
