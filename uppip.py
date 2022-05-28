#!/usr/bin/python3


import asyncio
import os
import subprocess
import time


async def main() -> None:
    start_time = time.time()
    print('pip upgrade')
    await upgrade_package('pip')
    print('pip is up to date')
    print('all packeges upgrade')
    package = await get_package()
    await asyncio.gather(*[upgrade_package(pack[0]) for pack in package.items()])
    await asyncio.sleep(0)
    await pprint()
    print("all packages is up to date")
    print(f'time is: {time.time() - start_time}')

async def get_package() -> dict:
    """
    Метод возращает словарь установленных пакетов.
    Где ключ - названия пакета. Значения его версия
    """
    key = list()
    val = list()
    temp_list = subprocess.check_output(f"pip3 list", shell=True).decode().split()
    for el in range(4, len(temp_list)):
        key.append(temp_list[el]) if el % 2 == 0 else val.append(temp_list[el])
    return dict(zip(key, val))

async def pprint() -> None:
    os.system("pip3 list")

async def upgrade_package(package):
    subprocess.check_output(f"pip3 install --upgrade {package}", shell=True)


if __name__ == "__main__":
    asyncio.run(main())
