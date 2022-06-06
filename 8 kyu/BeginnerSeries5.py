# Beginner Series #5 Triangular Numbers

def is_triangular(t):
    n = 1
    while True:
        x = n * (n + 1) / 2
        if x == t:
            return True
        elif x > t:
            return False
        n +=1
