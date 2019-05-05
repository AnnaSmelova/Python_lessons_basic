__author__ = 'Смелова Анна Алексеевна'

import os
import shutil


# Функция создает директорию name в папке, из которой запущен данный скрипт
def create_dir(name):
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dir_path)
        print(f'Директория {name} успешно создана')
    except FileExistsError:
        print(f'Директория {name} уже существует')


# Функция удаляет директорию name из папки, из которой запущен данный скрипт
def delete_dir(name):
    dir_path = os.path.join(os.getcwd(), name)
    try:
        shutil.rmtree(dir_path)
        print(f'Директория {name} успешно удалена')
    except FileNotFoundError:
        print(f'Директория {name} не найдена в текущей директории')


# Функция отображает все директории и файлы текущей директории
def view_current_dir_dirs_and_files_list():
    print('Директории и файлы текущей директории:')
    return os.listdir(os.getcwd())


# Функция отображает только директории текущей директории
def view_current_dir_dirs_list():
    print('Директории текущей директории:')
    for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
        return dirnames


# Функция отображает только файлы (без папок) текущей директории
def view_current_dir_files_list():
    print('Файлы текущей директории:')
    for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
        return filenames


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


# Функция создает копию указанного файла
def copy_file(file_name):
    fsrc = os.getcwd()  # текущая директория
    dir_list = os.listdir(fsrc)  # список всех директорий в текущей директории
    if not file_name in dir_list:
        print('Указанный файл не найден. Копирование невозможно.')
        return
    new_name = f'{file_name}_copy'
    # Если целевая директория уже существует, добавляем '_copy' в конец, чтобы создать новую копию
    while new_name in dir_list:
        new_name = new_name + '_copy'
    file_path = os.path.join(fsrc, file_name)
    fdst = os.path.join(fsrc, new_name) # итоговая целевая директория
    try:
        shutil.copytree(file_path,fdst)
        print(f'Файл {file_name} был успешно скопирован в файл {new_name}')
    except shutil.SameFileError:
        print('Невозможно скопировать файл сам в себя')
    except FileExistsError:
        print(f'Данный файл {new_name} уже существует')


# Функция меняет текущую директорию на dir_name
def change_dir(dir_name):
    if dir_name == 'go_to_parent':
        path = os.path.split(os.getcwd())[0]
    else:
        path = os.path.join(os.getcwd(),dir_name)
    try:
        os.chdir(path)
        cur_dir = os.path.abspath(os.curdir)
        print(f'Текущая директория: {cur_dir}')
    except FileNotFoundError:
        print('Указанная директория не найдена в текущей директории.')
        print('Поиск в родительской директории...')
        parent_dir = os.path.split(os.getcwd())[0]
        parent_path = os.path.join(parent_dir,dir_name)
        try:
            os.chdir(parent_path)
            cur_dir = os.path.abspath(os.curdir)
            print(f'Текущая директория: {cur_dir}')
        except FileNotFoundError:
            print('Указанная директория не найдена.')


# Функция меняет текущую директорию на директорию по указанному пути
def change_dir_by_path(path):
    try:
        # Ищем по абсолютному пути
        os.chdir(path)
        cur_dir = os.path.abspath(os.curdir)
        print(f'Выполнен переход в директорию: {cur_dir}')
    except FileNotFoundError:
        # Если не нашли по абсолютному - ищем по относительному пути
        current_dir = os.getcwd()
        dest_path = os.path.join(current_dir, path)
        try:
            os.chdir(dest_path)
            cur_dir = os.path.abspath(os.curdir)
            print(f'Выполнен переход в директорию: {cur_dir}')
        except FileNotFoundError:
            print('Директория по указанному пути не найдена.')

