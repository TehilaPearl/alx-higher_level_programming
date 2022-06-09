#!/usr/bin/python3
def common_elements(set_1, set_2):

    first_list = set(set_1)
    sec_list = set(set_2)

    final_list = first_list & sec_list
    return final_list
