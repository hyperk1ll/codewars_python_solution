# Valid Parentheses


def valid_parentheses(string):
    count1 = 0
    count2 = 0
    
    for i in string:
        if i == "(":
            count1 += 1
        elif i == ")":
            count2 += 1
        if count1 - count2 < 0:
            return False
    
    return count1 - count2 == 0