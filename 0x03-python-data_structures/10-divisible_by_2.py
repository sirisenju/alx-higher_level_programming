#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    number = []

    for num in range(len(my_list)):
        if my_list[num] % 2 == 0:
            number.append(True)
        else:
            number.append(False)
    return (number)
