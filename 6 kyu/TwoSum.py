# Two Sum

def two_sum(numbers, target):
    n = len(numbers)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return i, j
