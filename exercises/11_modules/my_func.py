#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 10:08:38 2018

@author: manana
"""

def generate_access_config(access, psecurity=False):
    '''
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17 }

    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    '''

    access_template = [
        'switchport mode access', 'switchport access vlan',
        'switchport nonegotiate', 'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]

    port_security = [
        'switchport port-security maximum 2',
        'switchport port-security violation restrict',
        'switchport port-security'
    ]
    
    result = []
    
    for interface, vlan in access.items():
        result.append(interface)
        for command in access_template:
            if command == 'switchport access vlan':
                result.append(command + ' ' + str(access[interface])) 
            else:
                result.append(command)
        if psecurity:
            for command in port_security:
                result.append(command)
    
    return result
    



def generate_trunk_config(trunk):
    '''
    trunk - словарь trunk-портов, для которых необходимо сгенерировать конфигурацию

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    '''
    trunk_template = [
        'switchport trunk encapsulation dot1q', 'switchport mode trunk',
        'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
    ]
    
    result = []
    
    for interface, vlans in trunk.items():
        result.append(interface)
        for command in trunk_template:
            if command == 'switchport trunk allowed vlan':
                result.append(command + ' ' + ', '.join([str(vlan) for vlan in vlans])) 
            else:
                result.append(command)
    
    return result




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
