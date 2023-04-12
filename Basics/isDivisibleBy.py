# problem is that this loop and check every option when we know that from 0-1000 it can only go up in 7's
import timeit
def isDivisibleBy():

    for i in range(0, 1000):
        # print(i)
        if i % 7 == 0:
            # print("bang")
            divSeven = i
            # print(divSeven)
            sumDiv = 0
            for digit in str(i):
                sumDiv += int(digit)
            # print(sumDiv)
            if sumDiv % 3 == 0:
                print(i)

isDivisibleBy()
