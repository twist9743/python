# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28  в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
input_ip = input('Введите IP ')
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
