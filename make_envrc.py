#!/usr/bin/python


from os.path import isfile


if isfile('.env'):
    f_read = open('.env', 'r')
    data = [f'export {line.strip()}' for line in f_read.readlines()]
    f_read.close()
    f_write = open('.envrc', 'w')
    f_write.write('\n'.join(data))
    f_write.close()
else:
    print('Файл ".env" не найден')
