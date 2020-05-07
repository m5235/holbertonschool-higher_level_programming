#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    m = 0
    s = 0
    for i in range(len(my_list)):
        m += my_list[i][0] * my_list[i][1]
        s += my_list[i][1]
    return m / s
