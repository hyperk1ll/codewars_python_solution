# Find the middle element

def gimme(input_array):
    length = len(input_array)

    middle = length // 2

    if input_array[0] < input_array[middle] < input_array[-1]:
        return 1
    elif input_array[0] >  input_array[middle] > input_array[-1]:
        return 1
    elif input_array[0] <  input_array[-1] > input_array[middle]:
        return 0
    elif input_array[0] >  input_array[-1] < input_array[middle]:
        return 0
    else:
        return 2
