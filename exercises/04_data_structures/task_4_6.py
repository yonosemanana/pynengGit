# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

data_route = ospf_route.split()                                    
#print(data_route)

str_template = """
Protocol:              {0}
Prefix:                {1}
AD/Metric:             {2}
Next-Hop:              {3}
Last update:           {4}
Outbound Interface:    {5}
"""

data_route.remove("via")

str_formatted = str_template.format("OSPF", data_route[1], data_route[2].strip("[]"), data_route[3].strip(","), data_route[4].strip(","), data_route[5])
print(str_formatted)

