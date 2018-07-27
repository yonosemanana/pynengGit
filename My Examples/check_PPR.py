#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 03:07:38 2018

@author: manana
"""

import re

susp_links_table = []
susp_links_ppr = []
links_table = set()
links_ppr = set()


with open("Links_part1.txt") as f:
    for line in f:
        m = re.search('(AR\d+-\d+.[a-z]+)(?:, )((?:Fast|Gigabit|TenGigabit)Ethernet\d+/\d+)(?:.*) (SW\d+-AR\d+-\d+.[a-z]+)(?:, )(.*\d+).*', line)
        if m != None:
            t = tuple(m.groups())
            links_table.add(t)
        else:
            susp_links_table.append(line)

#print(susp_links_table)
#print(links_table)
#print("\n" * 5)
          
with open("PPR_part1.txt") as f:
    for line in f:
        m = re.search('\s?(AR\d+-\d+.[a-z]+)\s+\[((?:Fast|Gigabit|TenGigabit)Ethernet\d+/\d+)\]\s+(SW\d+-AR\d+-\d+.[a-z]+)\s+\[(.*)\].*', line)
        if m != None:
            t = tuple(m.groups())
            links_ppr.add(t)
        else:
            susp_links_ppr.append(line)            
#print(susp_links_ppr)          
#print(links_ppr)



if __name__ == '__main__':    
    print("Links that are in table but not in PPR")
    for s in links_table.difference(links_ppr):
        print(s)
    print()
    
    print("Links that are in PPR but not in table")    
    for s in links_ppr.difference(links_table):
        print(s)
    print()
        
    print("Suspicious links from table (i.e. links that doesn't match pattern AR - AR's port - SW - SW's port)")
    for l in susp_links_table:
        print(l)
    print()
    
    print("Suspicious links from PPR (i.e. links that doesn't match pattern AR - AR's port - SW - SW's port)")
    for l in susp_links_ppr:
        print(l)