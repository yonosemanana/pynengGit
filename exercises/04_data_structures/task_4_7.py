# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

MAC = 'AAAA:BBBB:CCCC'

MAC_PARTS = MAC.split(':')

RES = ""

for MAC_PART in MAC_PARTS:
   RES += bin(int(MAC_PART, 16))[2:]
   
print(RES)
print(len(RES))
