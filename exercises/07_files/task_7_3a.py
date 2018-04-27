# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac_template = "{:>5}    {}"
mac_vlan = {}

with open("CAM_table.txt") as file:
    for line in file:
        if line[0] == " " and line[1].isnumeric():
            vlan, mac, _, interface = line.split()
            l = mac_vlan.get(int(vlan), [])
            l.append(mac + "   " + interface)
            mac_vlan[int(vlan)] = l

#print(mac_vlan)
vlans = [vlan for vlan in mac_vlan.keys()]
#print(vlans)
vlans.sort()
for vlan in vlans:
    for mac_port in mac_vlan[vlan]:
        print(mac_template.format(vlan, mac_port))