#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 01:48:37 2018

@author: manana
"""

from sys import argv

#interface, vlan = argv[1:]

interface = input("Enter the interface: ")
vlan = input("Enter the VLAN number: ")

access_template = ["switchport mode access", 
                   "switchport access vlan {}",
                   "switchport nonegotiate",
                   "spanning-tree port-fast",
                   "spanning-tree bpdu guard"]

print("\n" + "-" * 50)
print("interface {}".format(interface))
print("\n".join(access_template).format(vlan))

