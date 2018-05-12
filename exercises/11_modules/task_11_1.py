# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def parse_cdp_neighbors(listing):
    """
    The function returns a dictionary of pairs ('<device>', '<port>') for existing links between devices.
    Keys and values in the dictionary are tuples of strings, first element in the tuple is a device name and the second one - the device's interface.
    As input the function gets a string - an output of the 'show cdp neighbors' command.
    """
    
    result = {}
    
    lines = listing.split('\n')
    
    startData = False
    for line in lines:
        #print(line)
        if 'show cdp neighbors' in line:
            dev_name, *other = line.partition('>')
        elif 'Device ID' in line:
            startData = True
            continue
        elif startData and line != '':    
            neigh_name, dev_port_type, dev_port_number, *other, neigh_port_type, neigh_port_number = line.split()
            #print(line.split())
            #print(dev_port_type, dev_port_number)
            result[(dev_name, dev_port_type + dev_port_number)] = (neigh_name, neigh_port_type + neigh_port_number)
            
    return result 


if __name__ == '__main__':
    with open("sw1_sh_cdp_neighbors.txt") as f:
        listing = f.read()
    
    d = parse_cdp_neighbors(listing)
    print(d)    