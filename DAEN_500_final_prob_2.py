#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 05:18:34 2020

@author: braddyer
"""

class Input_and_shout:
    def __init__(self):
        self.input = str(input('Enter the phrase you would like me to shout: ').upper())
        
    def __str__(self):
        return 'Plug your ears... {}!!' .format(self.input)
        
usr_string = Input_and_shout()
print(usr_string)