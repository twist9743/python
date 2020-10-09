# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
table_mac = open('CAM_table.txt', 'r')
user_vlan = input('Введите Vlan: ')
for line in table_mac:
    output_table = table_mac.readlines()[5:]
for i in range(len(output_table)):
    output_table[i] = output_table[i].split()
    output_table[i].pop(2)
for i in range(len(output_table)):
    if output_table[i][0] == user_vlan:
        print("{:<6}{:<15}{:<6}".format(*output_table[i]))
table_mac.close()
