# How good are you really?

def better_than_average(class_points, your_points):
    a = sum(class_points) // len(class_points)
    
    if your_points > a:
        return True
    else:
        return False
