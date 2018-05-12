# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''



def get_int_vlan_map(config_filename):
    """
    The function gets a string - a name of the configuration file of a Cisco switch.
    The function returns two dictionaries - access ports and trunk ports in formats:
    Access:
    {'FastEthernet0/12':10,
     'FastEthernet0/14':11,
     'FastEthernet0/16':17}
    Trunk:
    {'FastEthernet0/1':[10,20],
     'FastEthernet0/2':[11,30],
     'FastEthernet0/4':[17]}
    """
    
    access_ports = {}
    trunk_ports = {}
    
    with open(config_filename) as f:
        for line in f:
            if line.find('interface') == 0:
                _, interface = line.split()
                allowed_vlan_command = False
            elif 'switchport mode access' in line:
                # When there is no command "switchport access vlan" in the config and there is command "switchport mode access", default VLAN 1 is assigned to the port.
                access_ports[interface] = 1
            elif 'switchport access vlan' in line: 
                # In config command "switchport mode access" always goes before command "switchport access vlan" and if this second one presents, vlan is overwritten.
                *other, vlan_str = line.split()
                vlan = int(vlan_str)
                access_ports[interface] = vlan
            elif 'switchport trunk allowed vlan' in line:
                allowed_vlan_command = True # A flag that command "switchport trunk allowed vlan" presents for the given interface
                _, _, _, _, vlans_str = line.split()
                if vlans_str == 'none':
                    trunk_ports[interface] = []
                else:
                    vlan_list_s = vlans_str.split(',')
                    trunk_ports[interface] = []
                    for vlan_s in vlan_list_s:
                        if '-' in vlan_s:
                            first, last = vlan_s.split('-')
                            trunk_ports[interface] += [vlan for vlan in range(int(first), int(last) + 1)]
                        else:
                            trunk_ports[interface] += [int(vlan_s)]
            elif 'switchport mode trunk' in line and not allowed_vlan_command:
                # When there is no command "switchport trunk allowed vlan" in the config and there is command "switchport mode trunk", all vlans are allowed.
                trunk_ports[interface] = [vlan for vlan in range(1, 4095)]
     
    return access_ports, trunk_ports              


                
access_ports, trunk_ports = get_int_vlan_map("config_sw2.txt")                
print("Access:")
print(access_ports)
print()
print("Trunk:")
print(trunk_ports)
