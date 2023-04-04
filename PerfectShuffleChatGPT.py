import time
import timeit


def perfect_shuffle(deck):
    # split the deck into two equal halves
    half = len(deck) // 2
    left_half = deck[:half]
    right_half = deck[half:]
    shuffled_deck = []
    # interleave the halves perfectly
    for i in range(half):
        shuffled_deck.append(left_half[i])
        shuffled_deck.append(right_half[i])
    # return the shuffled deck
    return shuffled_deck


print(
    timeit.timeit(stmt='perfect_shuffle([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])', setup='from __main__ import perfect_shuffle',
                  timer=time.perf_counter, number=5000000, globals=None))

# 3.0580030999844894 GPT

# 2.957373999990523 Kent