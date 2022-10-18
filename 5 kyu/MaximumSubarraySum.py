# Maximum subarray sum

def max_sequence(arr):
    if len(arr) == 0:
        return 0
    else:
        max_sum = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if sum(arr[i:j+1]) > max_sum:
                    max_sum = sum(arr[i:j+1])
        return max_sum