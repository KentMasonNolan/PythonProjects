INFILE = open("words.txt", 'r')
line = INFILE.readline()
wordlist = line.split()
TotalCount = 0

for words in line:
    for characters in words:
        print(ord(characters))
        TotalCount += 1

print(TotalCount)