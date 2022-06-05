# You only need one - Beginner

# Answer 1
def check(seq, elem):
    return elem in seq
  
# Answer 2
def check(seq, elem):
    for x in seq:
        if elem in seq:
            return True
        else:
            return False
