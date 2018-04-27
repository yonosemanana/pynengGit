# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

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

with open(argv[2], "w") as output_file:
    output_file.write(COMMANDS)
