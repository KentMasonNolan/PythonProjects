INFILE = open("euler.txt", 'r')
line = INFILE.readline()

print(line)

euler = [x for x in str(line)]

print(euler)

for i in range(len(euler)-3):
    print("pants")