# Growth of a Population


def nb_year(p0, percent, aug, p):
    year = 0
    
    while (p0 < p):
        p0 = int(p0 * (percent/100 + 1)) + aug
        year += 1
        
    return year
