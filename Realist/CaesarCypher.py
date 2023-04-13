from string import ascii_lowercase

letters = list(ascii_lowercase)


def caesar_cypher_encrypt(s, key):
    output = ""
    for x in s:
        debug = ord(x)

        if 65 <= ord(x) + key <= 90:
            output += chr(ord(x) + key)
            continue

        elif ord(x) + key >= 90 and ord(x) <= 90:
            y = ((ord(x) + key) % 90) + 64
            output += chr(y)
            continue

        elif 65 >= ord(x) <= 90 and 97 >= ord(x) <= 122:
            output += x
            continue

        if 97 <= ord(x) + key <= 122:
            output += chr(ord(x) + key)
            continue

        elif ord(x) + key >= 122:
            y = ((ord(x) + key) % 122) + 96
            output += chr(y)
            continue

    print(output)
    return output


caesar_cypher_encrypt("Two", 13)


def caesar_cypher_decrypt(s, key):
    output = ""
    for x in s:
        debug = ord(x)

        #UpperCase
        if 65 <= ord(x) <= 90:
            if 65 <= ord(x) - key <= 90:
                output += chr(ord(x) - key)
                continue
            elif (ord(x) - key) <= 65:
                y = 90 - abs((ord(x) - key) - 64)
                output += chr(y)
                continue

        #UpperCase
        elif 97 <= ord(x) <= 122:
            if 97 <= ord(x) - key <= 122:
                output += chr(ord(x) - key)
                continue
            elif ord(x) - key <= 97:
                y = 122 - abs((ord(x) - key) - 96)
                output += chr(y)

        #Check for spaces
        elif 65 >= ord(x) <= 90 and 97 >= ord(x) <= 122:
            output += x
            continue


        # elif ord(x) - key >= 90 and ord(x) <= 90:
        #     y = (ord(x) % 90) + 65
        #     output += chr(y)
        #     continue

    print(output)
    return output


caesar_cypher_decrypt("Gjb", 13)
