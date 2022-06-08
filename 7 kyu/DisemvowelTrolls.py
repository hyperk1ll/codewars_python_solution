# Disemvowel Trolls

def disemvowel(str):
    vowels = "aiueoAIUEO"

    for character in vowels:
        str = str.replace(character, "")
    return str
