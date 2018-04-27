# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

line_template = """
Protocol:              {}
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}
"""




#O        10.0.91.0/24 [110/60] via 10.0.19.9, 3d19h, FastEthernet0/2

with open("ospf.txt") as file:
    for line in file:
        print("\n" + "-" * 30)
        _, prefix, ad_metric, _, next_hop, update_time, interface = line.split()  
        protocol = "OSPF"
        ad_metric = ad_metric.strip("[]")
        next_hop = next_hop.strip(",")
        update_time = update_time.strip(",")

        line_formatted = line_template.format(protocol, prefix, ad_metric, next_hop, update_time, interface)
        print(line_formatted)
        
