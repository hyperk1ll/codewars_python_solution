# Even numbers in an array

def even_numbers(arr,n):
    x = [i for i in arr if i % 2 == 0]
    return x[-n:]