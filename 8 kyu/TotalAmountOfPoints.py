# Total amount of points

def points(games):
    score = 0
    
    for i in games:
        temp = i.split(':')
    
        x = int(temp[0])
        y = int(temp[1])
    
        if x > y:
            score += 3
        elif x == y:
            score += 1
    
    return score
