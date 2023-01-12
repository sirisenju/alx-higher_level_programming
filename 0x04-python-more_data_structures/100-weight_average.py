#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    den = 0
    for n in my_list:
        num += n[0] * n[1]
        den += n[1]
    return (num / den)
