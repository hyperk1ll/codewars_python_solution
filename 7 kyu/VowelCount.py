# Vowel Count

import re

def get_count(sentence):
    a = len(re.findall("a", sentence))
    i = len(re.findall("i", sentence))
    u = len(re.findall("u", sentence))
    e = len(re.findall("e", sentence))
    o = len(re.findall("o", sentence))
    return a + i + u + e + o
