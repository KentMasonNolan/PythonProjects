from string import ascii_lowercase

letters = list(ascii_lowercase)

def caesar_cypher_encrypt(s, key):
    output = ""
    for x in list(s):

        if 97 <= ord(x) + key <= 122:
            # print(chr(ord(x) + key))
            output += chr(ord(x) + key)
        elif ord(x) + key >= 122:
            y = (ord(x) % 122) + 97
            # print(y)
            output += chr(y)
        else:
            output += x
    print(output)
    return output


caesar_cypher_encrypt("Hello world$$z", 3)
