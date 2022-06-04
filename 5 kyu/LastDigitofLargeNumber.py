# Last digit of a large number

# Answer 1
def last_digit(n1, n2):
    
    if n2 == 0:
        return 1

    last_digits = []
    
    step = 1
    while True:
        number = pow(n1, step)
        step += 1
        last_digit = int(str(number)[-1])
        
        if last_digit in last_digits:
            break
        
        last_digits.append(last_digit)
    
    print(last_digits)
    last_digit_index = n2 % len(last_digits) - 1
    
    return last_digits[last_digit_index]

# Answer 2
def last_digit(n1, n2):
    return pow( n1, n2, 10 )