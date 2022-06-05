# Count characters in your string

# The main idea is to count all the occurring characters in a string. 
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}. 
# What if the string is empty? Then the result should be empty object literal, {}.

# Answer 1
def count(string):
    if len(string) == 0:
        return {}
    else:
        str = {}
        for char in set(string):
            str[char] = string.count(char)
        return str

# Answer 2

from collections import Counter

def count(string):
    return Counter(string)
