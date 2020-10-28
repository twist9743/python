# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess

list_of_ips = ["1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"]


def ping_ip_addresses(ip_list):
    availiable_ip = []
    unavailiable_ip = []
    for ip in ip_list:
        reply = subprocess.run(['ping', ip])
        if reply.returncode == 0:
            availiable_ip.append(ip)
        else:
            unavailiable_ip.append(ip)
    return availiable_ip, unavailiable_ip


print(ping_ip_addresses(list_of_ips))
