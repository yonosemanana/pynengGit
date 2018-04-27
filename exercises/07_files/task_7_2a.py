# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

COMMANDS = ""

with open(argv[1]) as file:
    
    for line in file:
        
        if not line.startswith("!"):
            
            PROHIBITED = False
            for word in ignore:
                if line.find(word) != -1:
                    PROHIBITED = True
                    break
            
            if not PROHIBITED:
                COMMANDS += line

print(COMMANDS)
