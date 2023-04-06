INFILE = open("euler.txt", 'r')
line = INFILE.readline()

print(line)

euler = [x for x in str(line)]

print(euler)

largestProduct = 0
for i in range(len(euler)-13):
    currentProduct = int(euler[i])
    for j in range(12):
        currentProduct = currentProduct * int(euler[i+j])

    if currentProduct > largestProduct:
        largestProduct = currentProduct

print(largestProduct)