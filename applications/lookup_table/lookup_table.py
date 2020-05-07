import math
import random

cache = {}


def somemath(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster

    # Check to see if (x,y) is in the cache,
    if (x, y) not in cache:
        # If not, store (x,y) as key, run function, and store result as the value
        cache[(x, y)] = somemath(x, y)

    # If it is, returns value
    return cache[(x, y)]


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
