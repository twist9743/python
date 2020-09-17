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
InputIp = input('Введите IP ')
UserIp = InputIp[:InputIp.find('/')]
Mask = InputIp[InputIp.find('/'):]
UserIp = UserIp.split('.')
MaskNumber = "1"*int(Mask.replace('/', '')) + \
    (32-int(Mask.replace('/', '')))*"0"
MaskNumber = MaskNumber[0:8] + ' ' + MaskNumber[8:16] + \
    ' ' + MaskNumber[16:24] + ' ' + MaskNumber[24:32]
MaskNumber = MaskNumber.split()
print(f'''
     Network:
     {int(UserIp[0]):<8} {int(UserIp[1]):<8} {int(UserIp[2]):<8} {int(UserIp[3]):<8}
     {int(UserIp[0]):08b} {int(UserIp[1]):08b} {int(UserIp[2]):08b} {int(UserIp[3]):08b}
     Mask:
     {Mask:<8}
     {int(MaskNumber[0],2):<8} {int(MaskNumber[1],2):<8} {int(MaskNumber[2],2):<8} {int(MaskNumber[3],2):<8}
     {MaskNumber[0]:<8} {MaskNumber[1]:<8} {MaskNumber[2]:<8} {MaskNumber[3]:<8}
     ''')
