def flatten(a_list):
    outputList = []
    for i in range(len(a_list)):
        for j in range(len(a_list[i])):

            outputList.append(a_list[i][j])
    print(outputList)
    return outputList


g = [[1, 2, 4], [[6]], [1, 2, 3, 4], [2, 3, 4, 5]]


flatten(g)