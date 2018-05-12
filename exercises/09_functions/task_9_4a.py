# -*- coding: utf-8 -*-
'''
Задание 9.4a

Задача такая же, как и задании 9.4.
Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам.
Она должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками

Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.

На примере interface Ethernet0/3.100:

{'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}}


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']


def check_ignore(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет

    '''
    return any(word in command for word in ignore)

def count_start_spaces(s):
    '''
    The function returns the number of starting spaces of the string s.
    '''  
    n = 0
    for c in s:
        if c != ' ':
            break
        else:
            n += 1
            
    return n


def parse_config_to_dict(config_filename):
    """
    The function gets the name of the configuration file.
    If there are two levels of subcommands, first level is a dictionary and the second is a list.
    If there are three levels of subcommands, first and second levels are dictionaries and the third is a list.
    The function ignores lines started with '!' and containing words from the ignore list.
    """
    
    '''
    THIS FUNCTION AND THIS PROGRAM IN GENERAL HAVEN'T BEEN COMPLETED YET!!!
    '''
    
    result = {}
    
    lines = []
    with open(config_filename) as f:
        for line in f:
            line = line.rstrip()
            if not line.lstrip().startswith('!') and not check_ignore(line, ignore):
                lines.append(line)
    
    #print(lines)
    
    buffer = [] # List of consequential string with the same depth level
    
    for i in range(len(lines)):
        #print(lines[i])
        
        if i == 0:
            pass
        elif count_start_spaces(lines[i]) > count_start_spaces(lines[i-1]):
            pass
        elif count_start_spaces(lines[i]) == count_start_spaces(lines[i-1]):
            buffer.append(lines[i])
        elif count_start_spaces(lines[i]) < count_start_spaces(lines[i-1]):
            pass
        elif i == len(lines)-1:
            pass
            

    return result

d = parse_config_to_dict("config_sw1.txt")
#print(d)
for command in d:
    print(command, d[command])
    
#print(count_start_spaces('  fadsfs '))