import time
import timeit

deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def perfect_shuffle(deck):
    half = int(len(deck) / 2)
    arrReturn = []
    for i in range(half):
        arrReturn.append(deck[i])
        arrReturn.append(deck[half+i])
    return arrReturn

perfect_shuffle(deck)

print(timeit.timeit(stmt='perfect_shuffle([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])', setup='from __main__ import perfect_shuffle', timer=time.perf_counter, number=5000000, globals=None))