import random
import numpy as np


def selectionSort(inputList):
    sortedComplete = False
    finalIndex = len(inputList) - 1
    startIndex = 0

    while not sortedComplete:
        sortedComplete = True

        while finalIndex != 1:
            for i in range(finalIndex):
                if inputList[startIndex] > inputList[startIndex + 1] and inputList[startIndex] != finalIndex:
                    inputList[startIndex], inputList[startIndex + 1] = inputList[startIndex + 1], inputList[startIndex]
                startIndex += 1
            finalIndex -= 1
            startIndex = 0

    return inputList


print(selectionSort([65, 45, 25, 55, 15, 10, 35]))

randnums = np.random.randint(1, 101, 100)

print("Before sort")
print(randnums)
print("After sort")
print(selectionSort(randnums))
