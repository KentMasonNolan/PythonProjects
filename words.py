INFILE = open("words.txt", 'r')
line = INFILE.readline()
wordlist = line.split()
print(wordlist)
count = 0
for words in line:
    count = count + words.count('e')

print(count)