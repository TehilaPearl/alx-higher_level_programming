#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import sys
    index = 0
    listed = (dir(hidden_4))
    listlen = len(listed)
    for elements in listed:
        if elements[0] == '_':
            continue
        else:
            print(elements)
