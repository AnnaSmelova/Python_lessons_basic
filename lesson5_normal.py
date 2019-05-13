__author__ = 'Смелова Анна Алексеевна'

# normal

print()
print('normal: Задание-1')
print()

'''
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
'''
import lesson5_easy_lib

def print_help():
    print('[0] - получение справки')
    print('[1] - перейти в папку')
    print('[2] - просмотреть содержимое текущей папки')
    print('[3] - удалить папку')
    print('[4] - создать папку')
    print('[5] - выход')

def go_to_dir(dir_name):
    while not dir_name:
        print('Если хотите перейти в родительскую директрию, укажите \"go_to_parent\".')
        print('Укажите имя директории: ')
        dir_name = input()
    lesson5_easy_lib.change_dir(dir_name)

def view_dir():
    print(lesson5_easy_lib.view_current_dir_dirs_and_files_list())

def delete_dir(dir_name):
    while not dir_name:
        print('Укажите имя директории: ')
        dir_name = input()
    lesson5_easy_lib.delete_dir(dir_name)

def create_dir(dir_name):
    while not dir_name:
        print('Укажите имя директории: ')
        dir_name = input()
    lesson5_easy_lib.create_dir(dir_name)

def print_error():
    print('Необходимо указать действие от 0 до 5.')
    print('Для получения справки укажите 0')
    print('Для выхода укажите 5.')

print_help()

flag = True
while flag:
    try:
        command = int(input('Укажите действие: '))
        flag = False
        while command != 5:
            if command == 0:
                print_help()
            elif command == 1:
                go_to_dir(None)
            elif command == 2:
                view_dir()
            elif command == 3:
                delete_dir(None)
            elif command == 4:
                create_dir(None)
            else:
                print_error()

            flag_2 = True
            while flag_2:
                try:
                    command = int(input('Укажите действие: '))
                    flag_2 = False
                except ValueError:
                    print_error()
    except ValueError:
        print_error()

