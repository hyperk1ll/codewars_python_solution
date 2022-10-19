# Help the bookseller !

def stock_list(listOfArt, listOfCat):
    if not listOfArt or not listOfCat:
        return ""
    else:
        return " - ".join(["({} : {})".format(i, sum([int(j.split()[1]) for j in listOfArt if j.startswith(i)])) for i in listOfCat])