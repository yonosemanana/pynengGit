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



def parse_config_to_dict(config_filename):
    """
    The function gets the name of the configuration file.
    If there are two levels of subcommands, first level is a dictionary and the second is a list.
    If there are three levels of subcommands, first and second levels are dictionaries and the third is a list.
    The function ignores lines started with '!' and containing words from the ignore list.
    """
    result = {}
    
    # For each command we should know a link to the dictionary, where the command is a key, and a link to its own dictionary.
    # All dictionaries must be parts of result {}.
    
    # And also we should know links to dictionaries for all levels of subcommands, and there must be latest commands.
    current_keys = {0: result}
    
    previous_level = 0 # A level for previous subcommand.
    previous_command = '' # A previous line in the configuration file
    
    with open(config_filename) as f:
           
        for line in f:
            
            line = line.rstrip() # Remove "\n" at the end of the line.
            if not line.startswith('!') and not check_ignore(line, ignore):
                
                # Find a number of spaces at the start of the string
                command_level = 0
                for c in line:
                    if c != ' ':
                        break
                    else:
                        command_level += 1
                #print()
                #print('command_level = ' + str(command_level))
                
                # Current command becomes the last command of its level.
                command = line.strip()
                #print('command = ' + command)
                
                # For each command find a dictionary where it should be placed
                
                #print('previous_level = '+ str(previous_level))
                #print(current_keys)
                
                if command_level > previous_level:
                    
                    d = {}
                    current_keys[previous_level][previous_command] = d
                    d[command] = []
                    
                    # Update current_keys dictionary with the current command
                    current_keys[command_level] = d  
 
                else:
                    # A command level is level or equal than the level of previous command.
                    
                    # Find the parent dictionary for the current command. It must be the highest level in current_keys but below the level of the command.
                    parent_level = 0
                    for key in current_keys:
                        if key > parent_level and key <= command_level:
                            parent_level = key
                    print('parent_level = ' + str(parent_level))
                    
                    l = []
                    current_keys[parent_level][command] = l
                    
                    # Update current_keys dictionary with the current command and delete all commands with higher levels.
                                
                    keys = [key for key in current_keys]
                    for key in keys:
                        if key > command_level:
                            current_keys.pop(key)
                    
                #print(current_keys)
                #print(result)
                
                previous_level = command_level
                previous_command = command

                
                #print(result)
    
    return result

d = parse_config_to_dict("config_sw1.txt")
#print(d)
for command in d:
    print(command, d[command])