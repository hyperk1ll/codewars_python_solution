# Calculating with Functions

def zero(a = None): return 0 if not a else a(0)
def one(a = None): return 1 if not a else a(1)
def two(a = None): return 2 if not a else a(2)
def three(a = None): return 3 if not a else a(3)
def four(a = None): return 4 if not a else a(4)
def five(a = None): return 5 if not a else a(5)
def six(a = None): return 6 if not a else a(6)
def seven(a = None): return 7 if not a else a(7)
def eight(a = None): return 8 if not a else a(8)
def nine(a = None): return 9 if not a else a(9)

def plus(y): return lambda x : x + y
def minus(y): return lambda x : x - y
def times(y): return lambda x : x * y
def divided_by(y): return lambda x : x // y
