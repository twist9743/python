# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ip = input('Введите IP - адрес: ')
bad = 'Неправильный IP-адрес'
if ip.count('.') != 3:
    print(bad)
else:
    ip = ip.split('.')
    for i in ip:
        try:
            if int(i) < 0 or int(i) > 255:
                print(bad)
        except ValueError:
            print(bad)
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
