#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 09:25:34 2018

@author: manana
"""

def print_int(n):
    """
    Function prints integer n and converts it to str before printing.
    """
    
    print(str(n))


print(__name__)
print("This is the code before \" if __name__ == '__main__' \" part")

if __name__ == '__main__':
    print("Inside the module")
    print("Thist is a test, n = 10")
    print_int(10)
    
    