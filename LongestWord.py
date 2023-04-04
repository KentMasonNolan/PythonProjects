import time
import timeit


def longest_word(text):
    lst = text.split()
    longest = 0
    if text == '':
        return ''
    for i in range(0, len(lst)):
        if len(lst[i]) > len(lst[longest]):
            longest = i
    return lst[longest]


longest_word("this is a list of longsword but the longest word is in the middle")
longest_word('You’ve got two empty halves of coconuts and you’re bangin’ em')

print(timeit.timeit(stmt='longest_word("this is a list of longsword but the longest word is in the middle")',
                    setup='from __main__ import longest_word', timer=time.perf_counter, number=1000000, globals=None))
