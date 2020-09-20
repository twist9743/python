# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
input_ip = input('Введите IP ')
user_ip = input_ip[:input_ip.find('/')]
mask = input_ip[input_ip.find('/')+1:]
user_ip = user_ip.split('.')
mask_number = "1"*int(mask) + \
    (32-int(mask))*"0"
mask_number = mask_number[0:8] + ' ' + mask_number[8:16] + \
    ' ' + mask_number[16:24] + ' ' + mask_number[24:32]
mask_number = mask_number.split()
print(f'''
     Network:
     {int(user_ip[0]):<8} {int(user_ip[1]):<8} {int(user_ip[2]):<8} {int(user_ip[3]):<8}
     {int(user_ip[0]):08b} {int(user_ip[1]):08b} {int(user_ip[2]):08b} {int(user_ip[3]):08b}
     Mask:
     /{mask:<8}
     {int(mask_number[0],2):<8} {int(mask_number[1],2):<8} {int(mask_number[2],2):<8} {int(mask_number[3],2):<8}
     {mask_number[0]:<8} {mask_number[1]:<8} {mask_number[2]:<8} {mask_number[3]:<8}
     ''')
