# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

COMMANDS = ""

with open(argv[1]) as input_file:    
    
    for line in input_file:            
        PROHIBITED = False
        for word in ignore:
            if line.find(word) != -1:
                PROHIBITED = True
                break
        if not PROHIBITED:
            COMMANDS += line

#print(COMMANDS)

with open("config_sw1_cleared.txt", "w") as output_file:
    output_file.write(COMMANDS)