#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 03:22:21 2018

@author: manana
"""
import re
from pprint import pprint


l = []
with open('dhcp_snooping_binding.txt') as f:
    for line in f:
        #m = re.search('(?P<MAC>([\w\d]{2}:){5}[\w\d]{2})\s+(?P<IP>(\d+\.){3}\d+)\s+\d+\s+[\w-]+\s+(?P<VLAN>\d+)\s+(?P<Interface>\S+)', line)     
        # Other way to do the same search.
        reg = re.compile('(?P<MAC>([\w\d]{2}:){5}[\w\d]{2})\s+(?P<IP>(\d+\.){3}\d+)\s+\d+\s+[\w-]+\s+(?P<VLAN>\d+)\s+(?P<Interface>\S+)')
        m = reg.search(line)
        
        if m != None:
            l.append(m.groupdict())
            
        
        
        ll = re.findall('(\S+).*(FastEthernet\d+/\d+) (\\1).*(\\2)', line)
        pprint(ll)
        
pprint(l)

