# Human Readable Time

# First Solution
def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    seconds = seconds - hours * 3600 - minutes * 60
    
    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

# Second Solution 
import datetime

def make_readable(seconds):
    x = datetime.datetime.fromtimestamp(seconds)
    
    h = seconds // 3600
    m = x.strftime('%M')
    s = x.strftime('%S')

    return f"{h:0>2}:{m}:{s}"