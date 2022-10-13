# Find The Parity Outlier

def find_outlier(integers):
    a = []
    b = []
    
    count1 = 0
    count2 = 0
    
    for i in integers:
        if i % 2 == 0:
            count1 += 1
            a.append(i)
            
        if i % 2 != 0:
            count2 += 1
            b.append(i)
            
    if count1 > count2:
        return b[0]
    else:
        return a[0]