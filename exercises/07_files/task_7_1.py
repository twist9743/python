# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
f = open('ospf.txt')
for line in f:
    ospf_string = line
    ospf_string = ospf_string.strip()
    ospf_string = ospf_string.replace('[', ' ')
    ospf_string = ospf_string.replace('via', ' ')
    ospf_string = ospf_string.replace(']', ' ')
    ospf_string = ospf_string.split()
    print(f'''
        Prefix {ospf_string[1]:<8} 
        AD/Metric {ospf_string[2]:<8} 
        Next-Hop {ospf_string[3]:<8} 
        Last update {ospf_string[4]:<8} 
        Outbound Interface {ospf_string[5]:<8} ''')
