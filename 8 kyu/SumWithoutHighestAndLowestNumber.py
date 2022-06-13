# Sum without highest and lowest number

def sum_array(arr):
    if arr == None:
        return 0
    elif len(arr) == 0 or len(arr) == 1 or len(arr) == 2:
        return 0
    elif len(arr) > 2:
        arr.sort()
        del arr[-1]
        del arr[0]
        return sum(arr)
