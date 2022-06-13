# Find the stray number

def stray(arr):
    n = len(arr)
    
    if arr[0] == arr[1] and arr[0] != arr[2]:
        return arr[2]
    elif arr[0] == arr[2] and arr[0] != arr[1]:
        return arr[1]
    elif arr[1] == arr[2] and arr[0] != arr[1]:
        return arr[0]

    for i in range(3, n):
        if arr[i] != arr[i - 1]:
            return arr[i]
    return arr[-1]
