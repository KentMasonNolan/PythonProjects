INFILE = open("11euler.txt", 'r')
line = INFILE.readline()
euler = [[None]*20]*20
for i in range(20):
    for j in range(20):
        euler[i][j] = line.split(' ')

    # euler[i] = int,x.strip().split(' ') for x in line

print(euler)
# for i in line:
#     euler.append()