# Who likes it?

def likes(names):
    a = len(names)
    
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        b = ','.join(names)
        return ("%s likes this" % b)
    elif len(names) == 2:
        b = ' and '.join(names)
        return ("%s like this" % b)
    elif len(names) == 3:
        b = ', '.join(names[0:2])
        c = ' '.join(names[2:3])
        return ("%s and %s like this" % (b, c))
    elif len(names) == 4:
        b = ', '.join(names[0:2])
        return ("%s and 2 others like this" % b)
    elif len(names) > 4:
        b = ', '.join(names[0:2])
        c = len(names) - 2
        return ("%s and %d others like this" % (b, c))
