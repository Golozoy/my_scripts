#!/usr/bin/python3


import os
import subprocess


def main() -> None:
    print('\npip upgrade\n')
    os.system("pip3 install --upgrade pip")
    print('\ndone\n')
    print('\nall packeges upgrade\n')
    package = get_package()
    upgrade_package(package)
    pprint()
    print("done")

def get_package() -> dict:
    """
    Метод возращает словарь установленных пакетов.
    Где ключ - названия пакета. Значения его версия
    """
    package = dict()
    key = list()
    val = list()
    temp_list = subprocess.check_output(f"pip3 list", shell=True).decode().split()
    for el in range(len(temp_list)):
        if el % 2 == 0:
            key.append(temp_list[el])
        else:
            val.append(temp_list[el])
    for el in range(len(key)):
        package[key[el]] = val[el]
    return package

def pprint() -> None:
    """
    Выводит список всех установленых пакетов и их версии
    """
    os.system("pip3 list")

def upgrade_package(packege: dict) -> None:
    for itm in packege.items():
        os.system(f"pip3 install --upgrade {itm[0]}")


if __name__ == "__main__":
    main()
