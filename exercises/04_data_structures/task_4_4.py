# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

tmp_str = command1[command1.find('1'):]
tmp_list = tmp_str.split(',')
set1 = set(int(c) for c in tmp_list)

tmp_str = command2[command2.find('1'):]
tmp_list = tmp_str.split(',')
set2 = set(int(c) for c in tmp_list)

int_set = set1.intersection(set2)
l = list(int_set)
print(l)