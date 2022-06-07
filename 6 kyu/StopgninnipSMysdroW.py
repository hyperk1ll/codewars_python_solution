

def spin_words(sentence):
    words = sentence.split()
    
    for word,i in enumerate(words):
        if len(i) > 4:
            words[word] = i[::-1]
        
    return ' '.join(words)
