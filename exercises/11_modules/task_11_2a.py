# -*- coding: utf-8 -*-
'''
Задание 11.2a

С помощью функции parse_cdp_neighbors из задания 11.1
и функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt


Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''


from draw_network_graph import draw_topology
from task_11_1 import parse_cdp_neighbors

file_names = ['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt',
              'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt']

net_topology = {}

for file in file_names:
    with open(file) as f:
        listing = f.read()
        next_topology = parse_cdp_neighbors(listing)

        # Remove existing links.
        for key in next_topology:
            if not key in net_topology.values():
                net_topology[key] = next_topology[key]

#print(net_topology)
draw_topology(net_topology)