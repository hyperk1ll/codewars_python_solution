# Rotate an array matrix

def rotate(matrix, direction): 
    if direction == "clockwise":
        return [list(i) for i in zip(*matrix[::-1])]
    elif direction == "counter-clockwise":
        return [list(i) for i in zip(*matrix)][::-1]