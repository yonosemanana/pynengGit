# -*- coding: utf-8 -*-
'''
Задание 5.1a

Всё, как в задании 5.1. Но, если пользователь ввел адрес хоста, а не адрес сети,
то надо адрес хоста преобразовать в адрес сети и вывести адрес сети и маску, как в задании 5.1.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


net = input("Enter the IP network in the format '10.1.1.0/24': ")

net_l = net.split("/")
ip_net = net_l[0]
ip_mask = net_l[1]





ip_net_l = [int(s) for s in ip_net.split(".")]


ip_template = "{0:08b}{1:08b}{2:08b}{3:08b}"
net_bin = ip_template.format(*ip_net_l)[:int(ip_mask)] + (32 - int(ip_mask)) * "0"
#print(net_bin)
ip_net_l = [int(net_bin[i*8:(i+1)*8], 2) for i in range(4)]

net_template = ("Network: \n"
                "{0:<8}  {1:<8}  {2:<8}  {3:<8}  \n"
                "{0:08b}  {1:08b}  {2:08b}  {3:08b}  \n")

#print(net_template.format(ip_net_l[0], ip_net_l[1], ip_net_l[2], ip_net_l[3]))
print(net_template.format(*ip_net_l))



mask_bin = "1" * int(ip_mask) + "0" * (32 - int(ip_mask))
#print(mask_bin)
ip_mask_l = [int(mask_bin[i*8:(i+1)*8], 2) for i in range(4)]
#print(ip_mask_l)

mask_template = ("Mask: \n"
                 "/{0} \n"
                "{1:<8}  {2:<8}  {3:<8}  {4:<8}  \n"
                "{1:08b}  {2:08b}  {3:08b}  {4:08b}  \n")

print(mask_template.format(ip_mask, *ip_mask_l))