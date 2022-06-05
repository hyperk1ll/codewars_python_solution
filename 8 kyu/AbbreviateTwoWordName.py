# Abbreviate a Two Word Name

def abbrev_name(name):
    names = name.split()
    return f"{names[0][:1]}.{names[1][:1]}".upper()
