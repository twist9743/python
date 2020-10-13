# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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
            elif vlans.find("duplex auto") == 1:
                vlans = 1
                access_dict[f'{interface}'] = vlans

    return access_dict, trunk_dict


print(get_int_vlan_map("config_sw2.txt"))
