# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]
f = open('config_sw1.txt')
g = open('onfig_sw1_cleared.txt', 'w')
for line in f:
    for i in range(len(ignore)):
        if line.find(ignore[i]) == -1:
            add_str = True
        else:
            add_str = False
            break
    if add_str == True:
        g.write(line)
