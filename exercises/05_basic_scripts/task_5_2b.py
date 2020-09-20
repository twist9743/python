# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv


input_ip = argv[1]
user_ip = input_ip[:input_ip.find('/')]
mask = input_ip[input_ip.find('/')+1:]
user_ip = user_ip.split('.')
mask_number = '1'*int(mask) + \
    (32-int(mask))*'0'
ip_bin = f"{int(user_ip[0]):08b}{int(user_ip[1]):08b}{int(user_ip[2]):08b}{int(user_ip[3]):08b}"
mask_number = mask_number[0:8] + ' ' + mask_number[8:16] + \
    ' ' + mask_number[16:24] + ' ' + mask_number[24:32]
ip_address = ip_bin[:mask_number.find('0')] + '0' * (32 - int(mask))
mask_number = mask_number.split()


ip_address = ip_address[0:8] + ' ' + ip_address[8:16] + \
    ' ' + ip_address[16:24] + ' ' + ip_address[24:32]
ip_address = ip_address.split()
print(f'''
     Network:
     {int(ip_address[0],2):<8} {int(ip_address[1],2):<8} {int(ip_address[2],2):<8} {int(ip_address[3],2):<8}
     {ip_address[0]:<8} {ip_address[1]:<8} {ip_address[2]:<8} {ip_address[3]:<8}
     Mask:
     /{mask:<8}
     {int(mask_number[0],2):<8} {int(mask_number[1],2):<8} {int(mask_number[2],2):<8} {int(mask_number[3],2):<8}
     {mask_number[0]:<8} {mask_number[1]:<8} {mask_number[2]:<8} {mask_number[3]:<8}
     ''')
