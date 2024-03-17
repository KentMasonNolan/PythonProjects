FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]


def printFlavours(inputValues):
    for i in range(len(inputValues) - 1):
        for j in range(len(inputValues) - i):
            if i != j+i:
                print(inputValues[i] + ", " + inputValues[j + i])


printFlavours(FLAVORS)
