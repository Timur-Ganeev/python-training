# Vectors
# Video
# Practice
import numpy as np
from pprint import pp
import random

x = np.array(range(0, 8, 3)) # np.arange(3) - in memory all, range(3) - generator
y = np.array(range(4, 7))

print(x)
print(y)

# print(type(x))
# print(x.max())
#
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(y ** x)
# print(y % x)

# pp(np.arange(6, 11))
# pp(np.full(4, 1))
# pp(np.full([3, 3], 0))

k = np.full(4, 0)
l = np.full(4, 1)

print(k)
print(l)

pp(np.concatenate((x, y)))
pp(np.concatenate((k, l)))
pp(np.concatenate((l, l)))

pp("--- shuffle ---")
a = np.arange(10)
random.shuffle(a)
pp(a)
