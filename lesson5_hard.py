__author__ = 'Смелова Анна Алексеевна'

# hard

print()
print('hard: Задание-1')
print()

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import lesson5_easy_lib
print('sys.argv = ', sys.argv)


def print_help():
    print('help - получение справки')
    print('mkdir <dir_name> - создание директории')
    print('ping - тестовый ключ')
    print('cp <file_name> - создание копию указанного файла')
    print('rm <file_name> - удаление указанного файла')
    print('cd <full_path or relative_path> - смена текущей директории на указанную')
    print('ls - отображение полного пути текущей директории')


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def copy_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    lesson5_easy_lib.copy_file(dir_name)

def remove_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    ans = input(f'Вы действительно хотите удалить файл {dir_name}? Укажите \'Y\', если да, и \'N\', если нет: ')
    if ans == 'Y':
        lesson5_easy_lib.delete_dir(dir_name)
    else:
        print('Команда отменена')
        return

def change_directory():
    if not dir_name:
        print("Необходимо указать путь к файлу вторым параметром")
        return
    lesson5_easy_lib.change_dir_by_path(dir_name)

def view_path():
    print(os.path.abspath(os.curdir))

do = {
    'help': print_help,
    'mkdir': make_dir,
    'ping': ping,
    'cp': copy_file,
    'rm': remove_file,
    'cd': change_directory,
    'ls': view_path
}

try:
    dir_name = ' '.join(sys.argv[2:])
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

