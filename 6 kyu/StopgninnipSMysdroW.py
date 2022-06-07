# Stop gninnipS My sdroW!

# Answer 1
def spin_words(sentence):
    words = sentence.split()
    
    for word,i in enumerate(words):
        if len(i) > 4:
            words[word] = i[::-1]
        
    return ' '.join(words)

# Answer 2
def spin_words(sentence):
    return ' '.join(x[::-1] if len(x) > 4 else x for x in sentence.split())
