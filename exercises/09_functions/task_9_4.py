# -*- coding: utf-8 -*-
"""
Задание 9.4

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    return any(word in command for word in ignore)


def convert_config_to_dict(config_filename):
    out_dict = dict()
    with open(config_filename, 'r') as f:
        str_file = f.readlines()
        for line in str_file:
            if ignore_command(line, ignore) == False and line[0] != "!" and line != "\n":
                if line.find(" ") != 0:
                    global_conf = line.strip()
                    out_dict.update({global_conf: []})
                else:
                    while line.find(" ") == 0:
                        out_dict[global_conf].append(line.strip())
                        line = f.readline()

    return out_dict


print(convert_config_to_dict(
    "C:/Users/User/Desktop/python/exercises/09_functions/config_sw1.txt"))
