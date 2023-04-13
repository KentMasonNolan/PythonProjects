from string import ascii_lowercase

letters = list(ascii_lowercase)


def caesar_cypher_encrypt(s, key):
    output = ""
    for x in s:

        if 65 <= ord(x) + key <= 90:
            # print(chr(ord(x) + key))
            output += chr(ord(x) + key)
        elif ord(x) + key >= 90 and ord(x) <= 90:
            y = (ord(x) % 90) + 65
            # print(y)
            output += chr(y)
        elif 65 >= ord(x) <= 90 and 97 >= ord(x) <= 122:
            output += x

        if 97 <= ord(x) + key <= 122:
            # print(chr(ord(x) + key))
            output += chr(ord(x) + key)
        elif ord(x) + key >= 122:
            y = (ord(x) % 122) + 97
            # print(y)
            output += chr(y)
    print(output)
    return output


caesar_cypher_encrypt("Hello world$$z", 3)
