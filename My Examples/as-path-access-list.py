#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 02:40:10 2018

@author: manana
"""

import re

line_template = "  ios-regex '{}',"
res = set()

sr33 = set("""  ios-regex '^(_196991)+$',
  ios-regex '^(_198449)+$',
  ios-regex '^(_198667)+$',
  ios-regex '^(_21275)+$',
  ios-regex '^(_3\.399)+$',
  ios-regex '^(_41082)+(_34561|_3\.820)*$',
  ios-regex '^(_49955)+$',
  ios-regex '^(_50119)+$',
  ios-regex '^(_51883)+$',
  ios-regex '^(_56947)+$',
  ios-regex '^(_59641)+$',
  ios-regex '^(_198258)+$',
  ios-regex '^(_201844)+$',
  ios-regex '^(_60600)+$',
  ios-regex '^(_60600)+(_44310|_197200)*$',
  ios-regex '^(_57898)+$',
  ios-regex '^(_199259)+$',
  ios-regex '^(_43237)+$',
  ios-regex '^(_43237)+(_30910)*$',
  ios-regex '^(_201643)+$',
  ios-regex '^(_41220)+$'""".split(','))

with open('as-path-access-list-2-old.txt') as f:
    for line in f:
        s = re.search('(\^.*\$)', line).group()
        res.add(line_template.format(s))
        print(line_template.format(s))

#print(res)
#print(sr33)
#print(res.difference(sr33))
#print(sr33.difference(res))
#        
