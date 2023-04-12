INFILE = open("../Basics/words.txt", 'r')
line = INFILE.readline()
wordlist = line.split()

letterFreq = [0] * 123
totalCount = 0

for words in line:
    for characters in words:
        if ord(characters) >= 97 & ord(characters) <= 122:
            totalCount += 1
            letterFreq[int(ord(characters))] = letterFreq[int(ord(characters))] + 1


for i in range(97,123):
    print(chr(i) + ":", "%.2f" % round(letterFreq[i] / totalCount, 2))
# for i in range(97,123):
#     print(chr(i) + ":", round(letterFreq[i] / totalCount, 2))

# print(totalCount)

