import time
import timeit


def longest_word(text):
    words = text.split()
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    # return the longest word
    return longest


print(timeit.timeit(stmt='longest_word("this is a list of longsword but the longest word is in the middle")',
                    setup='from __main__ import longest_word', timer=time.perf_counter, number=1000000, globals=None))
