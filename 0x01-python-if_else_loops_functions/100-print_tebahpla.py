#!/usr/bin/python3
for x in reversed(range(ord("a"), ord("z") + 1)):
    if x % 2 != 0:
        x = x - 32
    print("{:c}".format(x), end="")
