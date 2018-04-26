# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

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
ip_net_l = [int(s) for s in ip_net.split(".")]

net_template = ("Network: \n"
                "{0:<8}  {1:<8}  {2:<8}  {3:<8}  \n"
                "{0:08b}  {1:08b}  {2:08b}  {3:08b}  \n")

#print(net_template.format(ip_net_l[0], ip_net_l[1], ip_net_l[2], ip_net_l[3]))
print(net_template.format(*ip_net_l))


ip_mask = net_l[1]
mask_bin = "1" * int(ip_mask) + "0" * (32 - int(ip_mask))
#print(mask_bin)
ip_mask_l = [int(mask_bin[i*8:(i+1)*8], 2) for i in range(4)]
#print(ip_mask_l)

mask_template = ("Mask: \n"
                 "/{0} \n"
                "{1:<8}  {2:<8}  {3:<8}  {4:<8}  \n"
                "{1:08b}  {2:08b}  {3:08b}  {4:08b}  \n")

print(mask_template.format(ip_mask, *ip_mask_l))