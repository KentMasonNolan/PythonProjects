INFILE = open("euler.txt", 'r')
line = INFILE.readline()

print(line)

euler = [x for x in str(line)]

print(euler)

largestProduct = 0
for i in range(len(euler)-4):

    currentProduct = int(euler[i]) * int(euler[i+1]) * int(euler[i+2]) * int(euler[i+3])

    if currentProduct > largestProduct:
        largestProduct = currentProduct

print(largestProduct)