# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def get_int_vlan_map(config_filename):

    access_dict = dict()
    trunk_dict = dict()
    str_file = list()
    with open(config_filename, 'r') as f:
        str_file = f.readlines()
    for line in str_file:
        if line.find("FastEthernet") != -1:
            interface = line[line.find("FastEthernet"):].rstrip()
            vlans = str_file[str_file.index(line)+2]
            if vlans.find("switchport trunk allowed vlan") != -1:
                vlans = vlans[vlans.find("vlan")+4:]
                vlans = vlans.split(',')
                vlans = [int(elem) for elem in vlans]
                trunk_dict[f'{interface}'] = vlans
            elif vlans.find("switchport access vlan") != -1:
                vlans = int(vlans[vlans.find("vlan")+4:])
                access_dict[f'{interface}'] = vlans

    return access_dict, trunk_dict
