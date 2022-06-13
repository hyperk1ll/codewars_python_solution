# Counting Duplicates

def duplicate_count(text):
    if len(text) == 0:
        return 0
    else:
        a = text.lower()
        repeated = {}
        count = 0

        for i in range(0,len(a)):
            repeated[a[i]] = 0
        
        for key in repeated:
            for i in range(0,len(a)):
                if key == a[i]:
                    repeated[key] = repeated[key] + 1
        
        for key in repeated:
            if(repeated[key] > 1):
                count = count + 1
        return count
