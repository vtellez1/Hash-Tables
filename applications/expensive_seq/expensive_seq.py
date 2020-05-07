cache = {}


def exps(x, y, z):
    while x >= 0 and y >= 0 and z >= 0:
        if x <= 0:
            return y + z
        if x > 0:
            return expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)


def expensive_seq(x, y, z):
    # Check to see if (x, y, z) is in the cache
    if (x, y, z) not in cache:
        # If not, store (x,y,z) as key, run function, and store result as the value
        cache[(x, y, z)] = exps(x, y, z)

    # If it is, returns value
    return cache[(x, y, z)]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
