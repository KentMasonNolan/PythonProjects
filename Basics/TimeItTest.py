import timeit
import time

# print(timeit.timeit(stmt='', setup='', timer=time.perf_counter, number=1, globals=None))

# print(timeit.timeit(stmt='x=0', setup='', timer=time.perf_counter, number=1000000, globals=None))


print(timeit.timeit(stmt='x=0', setup='', timer=time.perf_counter, number=1000000, globals=None))
