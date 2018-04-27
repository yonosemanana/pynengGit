# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

user_vlan = input("Enter VLAN number: ")

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
    if vlan == int(user_vlan):
        for mac_port in mac_vlan[vlan]:
            print(mac_template.format(vlan, mac_port))