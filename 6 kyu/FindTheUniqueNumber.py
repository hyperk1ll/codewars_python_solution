# Find the unique number

def find_uniq(arr):
  n = len(arr)
  
  if n == 1:
    return -1

  if n == 2:
    return 0
 
  if arr[0] == arr[1] and arr[0] != arr[2]:
    return arr[2]
  if arr[0] == arr[2] and arr[0] != arr[1]:
    return arr[1]
  if arr[1] == arr[2] and arr[0] != arr[1]:
    return arr[0]
 
  for i in range(3, n):
    if arr[i] != arr[i - 1]:
      return arr[i]

  return arr[-1]
