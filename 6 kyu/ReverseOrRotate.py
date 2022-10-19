# Reverse or rotate?

def rev_rot(strng, sz):
    if sz <= 0 or strng == "" or sz > len(strng):
        return ""
    else:
        x = []
        
        for i in range(0, len(strng), sz):
            if len(strng[i:i+sz]) == sz:
                x.append(strng[i:i+sz])

        return "".join([i[::-1] if sum(int(j) for j in i) % 2 == 0 else i[1:] + i[0] for i in x])