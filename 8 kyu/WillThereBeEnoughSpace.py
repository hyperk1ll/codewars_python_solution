# Will there be enough space?

def enough(cap, on, wait):
    total_passanger = on + wait
    wait = total_passanger - cap
    if (total_passanger < cap):
        return 0
    else:
        return wait
