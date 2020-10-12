#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 08:21:51 2020

@author: braddyer
"""

# get user input of range for analysis
usr_range_start = int(input('Enter the low end of the range you want to try: '))
usr_range_end = int(input('Enter the high end of the range you want to try: '))

# determine the range -> add 1 to high end for inclusion
usr_range = range(usr_range_start, (usr_range_end + 1))

if usr_range_start <= usr_range_end:
  
# determine what numbers within range are divisible by 7 except those that are multiples of 5
    while usr_range_start in usr_range:
        if usr_range_start % 7 == 0 and usr_range_start % 5 != 0:
            print(usr_range_start)
            usr_range_start += 1
        else:
            usr_range_start += 1

# if second integer is less than the first
else:
    print('second integer can\'t be less than the first.\n')
