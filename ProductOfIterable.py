def mul(numbers):
    total = 1
    arrNumbers = list(numbers)
    for i in range(len(arrNumbers)):
        total = total * arrNumbers[i]
    return total


print(mul([1, 2, 3]))
