# Break camelCase

# Complete the solution so that the function will break up camel casing, using a space between words.

def solution(s):
    indent = ""
    for i in range(len(s)):
        char = s[i]
        if not char.isupper():
            indent += char
        else:
            indent += " " + char
    return indent
    