#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 07:03:42 2018

@author: manana
"""



with open("test_file.txt", "w") as f:
    print("Hello, world!", file=f)
    
print(1, 2, 3, sep=", ")

print(min(range(0, 5)), max(range(0,5)))
print(len(range(5)))

l = ['one', 'two', 'three', 'four']
m = sorted(l)
print(l, "id = " + str(id(l)))
print(m, "id = " + str(id(m)))



for indx, number in enumerate(l, 100):
    print(indx, number)
    
for i in range(len(l)):
    print(i+100, l[i])
    
    
form = ['first name', 'last name', 'telephone', 'address']
alex = ['Alex', 'Permyakov', '+79122023921', 'Uralskaya, 6-632']

d1 = dict()
for i in range(len(form)):
    d1[form[i]] = alex[i]
print(d1)

d2 = dict(zip(form, alex))
print(d2)
    

print(any(s.find('name') != -1 for s in form))
print(all(s.find('name') != -1 for s in form))