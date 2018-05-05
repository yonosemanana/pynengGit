#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 07:50:33 2018

@author: manana
"""

def plus(a, b):
    """
    Print arguments and returns the sum of two arguments.
    """
    print("a = {}, b = {}".format(a, b))
    return a + b

def plus_args(a, b, *args):
    """
    Print arguments and returns the sum of variable number of arguments.
    """
    print(args)
    x, *others = args
    print("a = {}, b = {}".format(a, b))
    return sum(args)

def plus_args1(*args, a, b):
    """
    Print arguments and returns the sum of variable number of arguments.
    """
    print(args)
    x, *others = args
    print("a = {}, b = {}".format(a, b))
    return sum(args)

def plus_kwargs(p, a, **kwargs):
    """
    Print arguments and returns the sum of variable number of keyword arguments.
    """ 
    print(kwargs)
#    x, *others = kwargs
#    print("a = {}, b = {}".format(a, b))
    return sum(kwargs.values())



print(plus(5, 10))
print("\n" + "-" * 30)
print(plus(10, 5))
print("\n" + "-" * 30)
print(plus(b=10, a=5))
print("\n" + "-" * 30)


l = [1, 2, 3, 4, 5]
print(plus_args(*l))
print("\n" + "-" * 30)
print(plus_args(10, 20, 30))
#print("\n" + "-" * 30)
#print(plus_args(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))
#print("\n" + "-" * 30)
#print(plus_args(10, 20, *(1000, 1000)))
#print("\n" + "-" * 30)
#
print(plus_args1(b=10, a=20, *(1000, 1000)))
print("\n" + "-" * 30)
#
#
#d = {"x": 10, "y" : 20, "z" : 30}
##print(plus_kwargs(**d))
#print("\n" + "-" * 30)
#print(plus_kwargs(5, b=1000, a=100, **d))
#print("\n" + "-" * 30)
#print(plus_kwargs(5, a=100, **d))
#print("\n" + "-" * 30)
#print(plus_kwargs(5, 1, c=100, **d))
#print("\n" + "-" * 30)