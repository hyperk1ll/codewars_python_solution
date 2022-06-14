# Ones and Zeros

def binary_array_to_number(arr):
    num = 0
    
    for i in arr:
        num = 2 * num + i
    
    return num
