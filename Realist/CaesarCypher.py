from string import ascii_lowercase

letters = list(ascii_lowercase)


def caesar_cypher_encrypt(s, key):
    output = ""
    for x in list(s):
        if ord(x) + key <= 122:
            print(chr(ord(x) + key))
            output += chr(ord(x) + key)
    print(output)


caesar_cypher_encrypt("hello world", 3)

print(ord('h') + 3)

# j = 97

# for i in range(97, 150):
#     print(chr(j))
#     j +=1
#     if j%123==0:
#         j=97
