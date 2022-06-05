# Beginner Series #3 Sum of Numbers

def get_sum(a,b):
    if a == b:
        return a
    elif a > b:
        return ((a *(a + 1)) / 2) - (((b - 1)* b) / 2)
    else:
        return ((b-a)+1) * (a + b) / 2
