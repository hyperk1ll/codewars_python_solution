# Directions Reduction

def dirReduc(arr):
    if len(arr) == 0:
        return arr
    for i in arr:
        if i not in ['NORTH', 'SOUTH', 'EAST', 'WEST']:
            return arr
    for i in range(len(arr)-1):
        if arr[i] == 'NORTH' and arr[i+1] == 'SOUTH':
            arr.pop(i)
            arr.pop(i)
            return dirReduc(arr)
        elif arr[i] == 'SOUTH' and arr[i+1] == 'NORTH':
            arr.pop(i)
            arr.pop(i)
            return dirReduc(arr)
        elif arr[i] == 'EAST' and arr[i+1] == 'WEST':
            arr.pop(i)
            arr.pop(i)
            return dirReduc(arr)
        elif arr[i] == 'WEST' and arr[i+1] == 'EAST':
            arr.pop(i)
            arr.pop(i)
            return dirReduc(arr)
    return arr