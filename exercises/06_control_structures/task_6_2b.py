# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Введите IP - адрес: ')
bad = 'Неправильный IP-адрес'
ip_correct = False
while not ip_correct:
    if ip.count('.') != 3:
        print(bad)
        ip = input('Введите IP - адрес еще раз: ')
    else:
        ip = ip.split('.')
        for i in ip:
            try:
                if int(i) < 0 or int(i) > 255:
                    print(bad)
                    ip = input('Введите IP - адрес еще раз: ')
            except ValueError:
                print(bad)
                ip = input('Введите IP - адрес еще раз: ')
        ip_correct = True
        if int(ip[0]) > 0 and int(ip[0]) < 224:
            print('unicast')
        elif int(ip[0]) > 223 and int(ip[0]) < 240:
            print('multicast')
        elif int(ip[0]) == 255 and int(ip[1]) == 255 and int(ip[2]) == 255 and int(ip[3]) == 255:
            print('local broadcast')
        elif int(ip[0]) == 0 and int(ip[1]) == 0 and int(ip[2]) == 0 and int(ip[3]) == 0:
            print('unassigned')
        else:
            print('unused')
