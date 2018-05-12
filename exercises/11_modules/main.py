#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 10:12:29 2018

@author: manana
"""

from my_func import generate_access_config, generate_trunk_config, get_int_vlan_map
from sys import argv

access_ports, trunk_ports = get_int_vlan_map(argv[1])

commands = generate_access_config(access_ports) + generate_trunk_config(trunk_ports)

with open("result.txt", "w") as f:
    for command in commands:
        f.write(command + "\n")
        