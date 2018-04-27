# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ASK_AGAIN = True

while ASK_AGAIN:
    IP_ADDR = input("Enter ip address in format '10.0.1.1': ")
    
    try:
        OCTETS = [int(IP) for IP in IP_ADDR.split(".")]
        
        if len(OCTETS) != 4:
            print("Incorrect IPv4 address")
        else:
            IN_RANGE = True
            for OCTET in OCTETS:
                if OCTET > 255 or OCTET < 0:
                    IN_RANGE = False
                    break
            if not IN_RANGE:
                print("Incorrect IPv4 addresses")
            else:
                FIRST_OCTET = int(OCTETS[0])
                if FIRST_OCTET >= 1 and FIRST_OCTET <= 223:
                    print("unicast")
                elif FIRST_OCTET >= 224 and FIRST_OCTET <= 239:
                    print("multicast")
                elif IP_ADDR == "0.0.0.0":
                    print("unassigned")
                elif IP_ADDR == "255.255.255.255":
                    print("local broadcast")
                else:
                    print("unused")
                ASK_AGAIN = False            
    except ValueError:
        print("Incorrect IPv4 address")
