# Find the smallest integer in the array

# Answer 1
def find_smallest_int(arr):
    arr.sort()
    return arr[0]

# Answer 2
def find_smallest_int(arr):
    return min(arr)
