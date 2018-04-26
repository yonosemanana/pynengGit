#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv


net = argv[1]

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