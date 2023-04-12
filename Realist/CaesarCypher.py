from string import ascii_lowercase

letters = list(ascii_lowercase)

# print(letters)

# a = "a"
# aascii = ord(a)
# aascii += 2
# print(aascii)

j = 97

for i in range(97, 150):
    print(chr(j))
    j +=1
    if j%123==0:
        j=97

