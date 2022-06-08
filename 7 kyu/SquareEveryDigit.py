# Square Every Digit

def square_digits(num):
    a = [int(x) for x in str(num)]
    b = [i * i for i in a]

    res = int("".join(map(str, b)))
    return res
