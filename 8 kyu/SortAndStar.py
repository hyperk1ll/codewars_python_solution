# Sort and Star

def two_sort(array):
    array.sort()
    a = "".join(i + '***' for i in array[0])
    
    return a[:-3]
