import random


def BubbleSort(toSort):
    bubbleSorted = False
    listLength = len(toSort) - 1
    print(len(toSort))

    while not bubbleSorted:
        bubbleSorted = True
        for i in range(listLength):
            if toSort[i] > toSort[i + 1]:
                toSort[i], toSort[i + 1] = toSort[i + 1], toSort[i]
                bubbleSorted = False
        listLength -= 1
    print(toSort)
    return toSort

# def bubble_sort(list):
#     unsorted_until_index = len(list) - 1
#     sorted = False
#     while not sorted:
#         sorted = True
#         for i in range(unsorted_until_index):
#             if list[i] > list[i+1]:
#                 list[i], list[i+1] = list[i+1], list[i]
#                 sorted = False
#             unsorted_until_index -= 1
#     return list
#
# # BubbleSort()
#
# print(bubble_sort([65, 55, 45, 35, 25, 15, 10]))

BubbleSort([65, 55, 45, 25, 15, 10, 35])

# for i in range(10):
#     returnList=[]
#     returnList[i] = random.randrange(1, 100, 1)
#     print(returnList[i])
#
# print(returnList)
