__author__ = 'Смелова Анна Алексеевна'

# easy

print('easy: Задание-1')
print()

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil

# Функция создает директории dir_1 - dir_9 в папке, из которой запущен данный скрипт
def create_9_dirs():
    for i in range(9):
        dir_path = os.path.join(os.getcwd(), f'dir_{i + 1}')
        try:
            os.mkdir(dir_path)
            print(f'Директория dir_{i + 1} успешно создана')
        except FileExistsError:
            print(f'Директория dir_{i + 1} уже существует')

# Функция удаляет директории dir_1 - dir_9 из папки, из которой запущен данный скрипт
def delete_9_dirs():
    for i in range(9):
        dir_path = os.path.join(os.getcwd(), f'dir_{i + 1}')
        try:
            shutil.rmtree(dir_path)
            print(f'Директория dir_{i + 1} успешно удалена')
        except FileNotFoundError:
            print(f'Директория dir_{i + 1} не найдена')

create_9_dirs()
delete_9_dirs()

print()
print('easy: Задание-2')
print()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os

# Функция отображает все директории и файлы текущей директории
def view_current_dir_dirs_and_files_list():
    files_list = os.listdir(os.getcwd())
    print('Директории и файлы текущей директории:')
    for k in files_list:
        print(k)

view_current_dir_dirs_and_files_list()

# Функция отображает только директории текущей директории
def view_current_dir_dirs_list():
    print('Директории текущей директории:')
    for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
        for k in dirnames:
            print(k)
        break

view_current_dir_dirs_list()

# Функция отображает только файлы (без папок) текущей директории
def view_current_dir_files_list():
    print('Файлы текущей директории:')
    for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
        for k in filenames:
            print(k)
        break

view_current_dir_files_list()

print()
print('easy: Задание-3')
print()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os
import shutil

# Функция создает копию дирректории, из которой был запущен данный скрипт
def copy_current_dir():
    fsrc = os.getcwd() # текущая директория
    parent_dir = os.path.split(fsrc)[0] # директория, родительская к текущей
    new_name = f'{os.path.split(fsrc)[1]}_copy' # имя копии директории
    dir_list = os.listdir(parent_dir) # список всех директорий в родительской директории
    # Если целевая директория уже существует, добавляем '_copy' в конец, чтобы создать новую копию
    while new_name in dir_list:
        new_name = new_name + '_copy'
    fdst = os.path.join(parent_dir, new_name) # итоговая целевая директория
    try:
        shutil.copytree(fsrc,fdst)
        print(f'Директория {fsrc} была успешно скопирована в директорию {fdst}')
    except shutil.SameFileError:
        print('Невозможно скопировать файл сам в себя')
    except FileExistsError:
        print(f'Данная директория {fdst} уже существует')

copy_current_dir()