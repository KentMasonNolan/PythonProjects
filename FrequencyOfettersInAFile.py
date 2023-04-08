INFILE = open("words.txt", 'r')
line = INFILE.readline()
wordlist = line.split()
TotalCount = 0

for words in line:
    for characters in words:
        if ord(characters) >= 97 & ord(characters) <= 122:
            # print(ord(characters))
            TotalCount += 1

print(TotalCount)
a = "a"
b = "z"
print(ord(a))
print(ord(b))