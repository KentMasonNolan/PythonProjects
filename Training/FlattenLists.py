def flatten(a_list):
    outputList = []
    for i in a_list:
        for j in i:
            outputList.append(j)
    print(outputList)
    return outputList


g = [[1, 2, 4], [[6]], [1, 2, 3, 4], [2, 3, 4, 5]]


flatten(g)