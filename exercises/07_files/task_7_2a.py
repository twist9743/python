# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]
f = open('config_sw1.txt')
for line in f:
    for i in range(len(ignore)):
        if line[0] != '!' and line.find(ignore[i]) == -1:
            add_str = True
        else:
            add_str = False
            break
    if add_str == True:
        print(line.rstrip())
f.close()
