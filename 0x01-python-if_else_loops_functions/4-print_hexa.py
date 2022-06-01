#!/usr/bin/python3
# Printing numbers from 0-98 in decimal and hexadecimal.
for num in range(0, 99):
    print("{:d} = 0x{:x}".format(num, num))
