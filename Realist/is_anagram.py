# def is_anagram(left, right):
#     left = left.replace(" ", "").lower()
#
#     right = right.replace(" ", "").lower()
#
#     leftList = list(left)
#     for i in leftList:
#         if i.isalnum():
#             leftList[i]
#     print(leftList)
#
#     leftSet = set(list(left))
#     rightSet = set(list(right))
#     # print(leftSet)
#
#
#     if leftSet <= rightSet & rightSet <= leftSet:
#         print("true")
#         return True
#     else:
#         return False
#
#     # defaultCardsList = set(defaultCardsArr)
#     # cardsArr = str.split(cards)
#     # cardsList = set(cardsArr)
#     # missing = (set(defaultCardsList.difference(cardsList)))
#     # missingString = "".join(missing)
#     # return missingString
#
#
# is_anagram("crâné", "crâné")



import unicodedata

def is_anagram(str1, str2):
    str1 = unicodedata.normalize('NFKD', str1.lower().replace(" ", "").replace("'", "").replace("-", "").replace('"', ''))
    str2 = unicodedata.normalize('NFKD', str2.lower().replace(" ", "").replace("'", "").replace("-", "").replace('"', ''))
    str1 = ''.join(sorted(str1, key=lambda s: unicodedata.normalize('NFKD', s)))
    str2 = ''.join(sorted(str2, key=lambda s: unicodedata.normalize('NFKD', s)))
    return str1 == str2


is_anagram("nectar","cranté")
