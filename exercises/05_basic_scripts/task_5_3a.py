# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]


modes = {"access":access_template, "trunk":trunk_template}
vlan_question = {"access":"Enter VLAN number:", "trunk":"Enter allowed VLANs:"}

int_mode = input('Enter interface mode (access/trunk): ')
int_number = input('Enter interface type and number: ')
int_vlans = input(vlan_question[int_mode])


s = "interface {}\n".format(int_number)
s += "\n".join(modes[int_mode]).format(int_vlans)

print("\n" + "-" * 30)
print(s)