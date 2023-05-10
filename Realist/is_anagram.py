import unidecode

def is_anagram(left, right):
    left = left.replace(" ", "").lower()
    left = unidecode(left, "utf-8")

    right = right.replace(" ", "").lower()
    right = unidecode(right, "utf-8")

    leftSet = set(list(left))
    rightSet = set(list(right))
    # print(leftSet)


    if leftSet <= rightSet & rightSet <= leftSet:
        print("true")
        return True
    else:
        print("False")
        return False

    # defaultCardsList = set(defaultCardsArr)
    # cardsArr = str.split(cards)
    # cardsList = set(cardsArr)
    # missing = (set(defaultCardsList.difference(cardsList)))
    # missingString = "".join(missing)
    # return missingString


is_anagram("crâné", "crasdhasdcrânéne")
