import numpy as np
from time import perf_counter

input = """"""

example = """"""
















start = perf_counter()
result1 = task1(input, -50, 50)
stop = perf_counter()
elapsed1 = stop - start
start = perf_counter()
result2 = task2(input)
stop = perf_counter()
elapsed2 = stop - start

print(f"Task 1: {result1}")
print(f"Execution time: {elapsed1}s")
print("")
print(f"Task 1: {result2}")
print(f"Execution time: {elapsed2}s")