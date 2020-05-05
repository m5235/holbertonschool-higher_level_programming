#!/usr/bin/python3
def no_c(my_string):
    s = ""
    for x in my_string:
        if x == "c" or x == "C":
            continue
        s = s + x
    return s
