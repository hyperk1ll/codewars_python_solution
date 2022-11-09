# Safen User Input Part I - htmlspecialchars

def html_special_chars(data): 
    x = []
    
    for i in data:
        if i == ">":
            i ="&gt;"
            x.append(i)
        elif i == "<":
            i = "&lt;"
            x.append(i)
        elif i == '"':
            i = "&quot;"
            x.append(i)
        elif i == "&":
            i = "&amp;"
            x.append(i)
        else:
            x.append(i)
    
    return ''.join(x)