word = 'apple'
print(word)
word = list(word)
print(word)
n=0
word[n] = 'r'
print(word)
n +=1
word[n] = ' _'
print(word)
word = ''.join([str(elem) for elem in word])
print(word)