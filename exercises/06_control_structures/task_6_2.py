# -*- coding: utf-8 -*-
"""
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Введите IP - адрес: ')
ip = ip.replace('.', ' ')
ip = ip.split()
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
