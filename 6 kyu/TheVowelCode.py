# The Vowel Code

def encode(st):
    vowels = {"a":"1", 
              "e":"2", 
              "i":"3", 
              "o":"4", 
              "u":"5" }

    for i, j in vowels.items():
        st = st.replace(i.lower(), j)

    return st

    
def decode(st):
    vowels = {"1":"a", 
              "2":"e", 
              "3":"i", 
              "4":"o", 
              "5":"u" }

    for i, j in vowels.items():
        st = st.replace(i.lower(), j)

    return st