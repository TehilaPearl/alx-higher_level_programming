#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    index = 0
    copy_list = my_list[:]

    if (len(my_list)) == 0:
        return my_list

    if idx < 0:
        return my_list

    for elem in my_list:
        if index == idx:
            copy_list[index] = element
            return copy_list
        index += 1

    if idx >= index:
        return my_list
