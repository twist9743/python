# -*- coding: utf-8 -*-
"""
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Обратите внимание на vlan 1000 - он должен выводиться последним.
Правильной сортировки можно добиться, если vlan будет числом, а не строкой.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
table_mac = open('CAM_table.txt', 'r')
for line in table_mac:
    output_table = table_mac.readlines()[5:]
for i in range(len(output_table)):
    output_table[i] = output_table[i].split()
    output_table[i].pop(2)
for j in range(len(output_table)):
    for i in range(len(output_table)-1):
        if int(output_table[i][0]) > int(output_table[i+1][0]):
            dig_small = output_table[i+1][0]
            output_table[i+1][0] = output_table[i][0]
            output_table[i][0] = dig_small
for line in output_table:
    print("{:<6}{:<15}{:<6}".format(*line))
table_mac.close()
