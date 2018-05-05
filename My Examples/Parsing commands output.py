#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 03:20:55 2018

@author: manana

"""


"""
Get interfaces and ip addresses of the output of 'show ip interface brief'.
Only lines with assigned ip addresses are interesting.
Read data from file.
Returns a dictionary, where interfaces are keys and ip addresses are values.
"""

d = {}

with open("sh_ip_int_br.txt") as f:
    for line in f:
        l = line.split()
        if len(l) >= 2:
            if l[1][0].isdigit():
                #d[l[0]] = l[1] # There is a better way to do that
                interface, ip, *other = l
                d[interface] = ip
            
print(d)
print("\n" + "-" * 30)




"""
Get interfaces and MTUs of the output of 'show ip interface'.
Only interfaces with MTU are interesting.
Read data from file.
Returns a dictionary, where interfaces are keys and MTUs are values.
"""

d = {}

with open("show_ip_interface.txt") as f:
    for line in f:
        if line.find("is up, line protocol is up") != -1:
            l = line.split()
            interface, *other = l
        if line.find("MTU is") != -1:
            l = line.split()
            *other, mtu, _ = l
            d[interface] = mtu
print(d)
print("\n" + "-" * 30)



"""
Get interfaces, ip addresses and MTUs of the output of 'show ip interface'.
Only interfaces with MTU are interesting.
Read data from file.
Returns a dictionary, where interfaces are keys and values are other dictionaries with keys 'mtu' and 'ip' and corresponding values.
"""

d = {}

with open("show_ip_interface.txt") as f:
    for line in f:
        if "is up, line protocol is up" in line:
            l = line.split()
            interface, *other = l
            
            d[interface] = {}
            
        elif "Internet address" in line:
            l = line.split()
            *other, ip = l
            ind = ip.find("/")
            ip = ip[:ind]
            
            d[interface]["ip"] = ip
             
        elif "MTU is" in line:
            l = line.split()
            *other, mtu, _ = l
            
            d[interface]["mtu"] = mtu
        
            
print(d)
print("\n" + "-" * 30)