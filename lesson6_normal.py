__author__ = 'Смелова Анна Алексеевна'

# normal

print()
print('normal: Задание-1')
print()

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

import random


class Person:
    def __init__(self, name, second_name, surname, school):
        self.name = name
        self.second_name = second_name
        self.surname = surname
        self.school = school

    def get_fio(self):
        return self.surname.title() + ' ' + self.name[0].upper() + '.' + self.second_name[0].upper() + '.'


class Teacher(Person):
    def __init__(self, surname, name, second_name, school, subject, teach_classes=[]):
        Person.__init__(self, name, second_name, surname, school)
        self.subject = subject
        self.teach_classes = teach_classes


class Pupil(Person):
    def __init__(self, surname, name, second_name, school, class_room, mother, father):
        Person.__init__(self, name, second_name, surname, school)
        self.class_room = class_room
        self.mother = mother
        self.father = father


class School:
    def __init__(self, school, classes = []):
        self.school = school
        self.classes = classes


class Class:
    def __init__(self, school, class_room, pupils = [], teachers = []):
        self.school =  school
        self.class_room = class_room
        self.pupils = pupils
        self.teachers = teachers


class Subject:
    def __init__(self, school, subject, teacher=''):
        self.school =  school
        self.subject = subject
        self.teacher = teacher


# Создаем объект класса 'Школа'
school = School('Школа №1')

# Создаем объекты класса 'Класс'
classes = [Class('Школа №1', '1 А'),
           Class('Школа №1', '1 Б'),
           Class('Школа №1', '2 А'),
           Class('Школа №1', '3 Б'),
           Class('Школа №1', '4 А'),
           Class('Школа №1', '5 Г'),
           Class('Школа №1', '6 Б'),
           Class('Школа №1', '7 А'),
           Class('Школа №1', '9 Е')]

# Создаем объекты класса 'Предмет'
subjects = [Subject('Школа №1','Математика'),
            Subject('Школа №1','Биология'),
            Subject('Школа №1','Химия'),
            Subject('Школа №1','Информатика'),
            Subject('Школа №1','Русский язык'),
            Subject('Школа №1','Литература'),
            Subject('Школа №1','История')]


# Функция генерирует произвольное множество классов для преподавателя
# Возвращает множество наименований классов
def get_random_class_list(classes):
    classes = [k.class_room for k in classes]
    class_list = set()
    num = random.randint(1,9) # кол-во классов, в которых преподает учитель
    for _ in range(num):
        class_name = classes[random.randint(0,8)]
        class_list.add(class_name)
    return list(class_list)


# Создаем объекты класса 'Учитель'
teachers = [Teacher('Ковалевская', 'Софья', 'Васильевна', 'Школа №1', 'Математика', get_random_class_list(classes)),
            Teacher('Дарвин', 'Чарльз', 'Роберт', 'Школа №1', 'Биология', get_random_class_list(classes)),
            Teacher('Менделеев', 'Дмитрий', 'Иванович', 'Школа №1', 'Химия', get_random_class_list(classes)),
            Teacher('Касперский', 'Евгений', 'Валентинович', 'Школа №1', 'Информатика', get_random_class_list(classes)),
            Teacher('Даль', 'Владимир', 'Иванович', 'Школа №1', 'Русский язык', get_random_class_list(classes)),
            Teacher('Пушкин', 'Александр', 'Сергеевич', 'Школа №1', 'Литература', get_random_class_list(classes)),
            Teacher('Карамзин', 'Николай', 'Михайлович', 'Школа №1', 'История', get_random_class_list(classes))]

# Заполняем атрибут 'преподаватель' в объектах класса 'Предмет'
for subj in subjects:
    for teach in teachers:
        if subj.subject == teach.subject:
            subj.teacher = teach.get_fio()
            break

# Заполняем атрибут 'преподаватели' в объектах класса 'Класс'
for cl in classes:
    t = set()
    for teach in teachers:
        if cl.class_room in teach.teach_classes:
            t.add(teach.get_fio())
    cl.teachers = list(t)

# Создаем объекты класса 'Ученик'
pupils = [Pupil('Иванов', 'Иван', 'Иванович', 'Школа №1', '1 Б', 'Иванова Е.К.', 'Иванов И.П.'),
          Pupil('Первый', 'Ученик', 'Первого', 'Школа №1', '1 А', 'Первая М.А.', 'Первый П.А.'),
          Pupil('Второй', 'Ученик', 'Первого', 'Школа №1', '1 А', 'Вторая М.А.', 'Второй П.А.'),
          Pupil('Третий', 'Ученик', 'Первого', 'Школа №1', '1 Б', 'Третья М.А.', 'Третий П.А.'),
          Pupil('Четвертый', 'Ученик', 'Первого', 'Школа №1', '1 Б', 'Четвертая М.А.', 'Четвертый П.А.'),
          Pupil('Первый', 'Ученик', 'Второго', 'Школа №1', '2 А', 'Первая М.Б.', 'Первый П.Б.'),
          Pupil('Второй', 'Ученик', 'Второго', 'Школа №1', '2 А', 'Вторая М.Б.', 'Второй П.Б.'),
          Pupil('Первый', 'Ученик', 'Третьего', 'Школа №1', '3 Б', 'Первая М.В.', 'Первый П.В.'),
          Pupil('Второй', 'Ученик', 'Третьего', 'Школа №1', '3 Б', 'Вторая М.В.', 'Второй П.В.'),
          Pupil('Третий', 'Ученик', 'Третьего', 'Школа №1', '3 Б', 'Третья М.В.', 'Третий П.В.'),
          Pupil('Первый', 'Ученик', 'Четвертого', 'Школа №1', '4 А', 'Первая М.Г.', 'Первый П.Г.'),
          Pupil('Второй', 'Ученик', 'Четвертого', 'Школа №1', '4 А', 'Вторая М.Г.', 'Второй П.Г.'),
          Pupil('Первый', 'Ученик', 'Пятого', 'Школа №1', '5 Г', 'Первая М.Д.', 'Первый П.Д.'),
          Pupil('Второй', 'Ученик', 'Пятого', 'Школа №1', '5 Г', 'Вторая М.Д.', 'Второй П.Д.'),
          Pupil('Третий', 'Ученик', 'Пятого', 'Школа №1', '5 Г', 'Третья М.Д.', 'Третий П.Д.'),
          Pupil('Первый', 'Ученик', 'Шестого', 'Школа №1', '6 Б', 'Первая М.Е.', 'Первый П.Е.'),
          Pupil('Второй', 'Ученик', 'Шестого', 'Школа №1', '6 Б', 'Вторая М.Е.', 'Второй П.Е.'),
          Pupil('Первый', 'Ученик', 'Седьмого', 'Школа №1', '7 А', 'Первая М.Ж.', 'Первый П.Ж.'),
          Pupil('Первый', 'Ученик', 'Девятого', 'Школа №1', '9 Е', 'Первая М.З.', 'Первый П.З.'),
          Pupil('Второй', 'Ученик', 'Девятого', 'Школа №1', '9 Е', 'Вторая М.З.', 'Второй П.З.'),
          Pupil('Третий', 'Ученик', 'Девятого', 'Школа №1', '9 Е', 'Третья М.З.', 'Третий П.З.')]

# Заполняем атрибут 'ученики' в объектах класса 'Класс'
for cl in classes:
    t = set()
    for p in pupils:
        if cl.class_room == p.class_room:
            t.add(p.get_fio())
    cl.pupils = list(t)


def print_help():
    print('[0] - Получение справки по командам')
    print('[1] - Получить полный список всех классов школы')
    print('[2] - Получить список всех учеников в указанном классе')
    print('[3] - Получить список всех предметов указанного ученика')
    print('[4] - Узнать ФИО родителей указанного ученика')
    print('[5] - Получить список всех Учителей, преподающих в указанном классе')
    print('[6] - Выход')


# Получить полный список всех классов школы
def get_class_list():
    return [k.class_room for k in classes]


# Получить список всех учеников в указанном классе
def get_pupils_list():
    class_room = input('Укажите класс в формате "<цифра> <буква>": ')
    class_list = get_class_list()
    if class_room in class_list:
        l = [k.pupils for k in classes if k.class_room == class_room]
        for el in l:
            print(el)
    else:
        print('Такого класса нет в школе.')


# Получить список всех предметов указанного ученика
def get_subjects():
    pupil = input('Укажите ФИО ученика в формате "<Фамилия И.О.>": ')
    if pupil in [k.get_fio() for k in pupils]:
        for k in pupils:
            if k.get_fio() == pupil:
                class_room = k.class_room
                break
        for m in classes:
            if class_room == m.class_room:
                teachs = m.teachers
                break
        subj_list = []
        for t in teachs:
            for n in teachers:
                if t == n.get_fio():
                    subj_list.append(n.subject)
                    break
        print(subj_list)
    else:
        print('Такого ученика нет в школе.')


# Узнать ФИО родителей указанного ученика
def get_parents_names():
    pupil = input('Укажите ФИО ученика в формате "<Фамилия И.О.>": ')
    if pupil in [k.get_fio() for k in pupils]:
        for p in pupils:
            if pupil == p.get_fio():
                print(p.mother + ' / ' + p.father)
                break
    else:
        print('Такого ученика нет в школе.')


# Получить список всех Учителей, преподающих в указанном классе
def get_class_teachers():
    class_room = input('Укажите класс в формате "<цифра> <буква>": ')
    class_list = get_class_list()
    if class_room in class_list:
        l = [k.teachers for k in classes if k.class_room == class_room]
        for el in l:
            print(el)
    else:
        print('Такого класса нет в школе.')


def print_error():
    print('Необходимо указать действие от 0 до 6.')
    print('Для получения справки укажите 0')
    print('Для выхода укажите 6.')


print_help()

flag = True
while flag:
    try:
        command = int(input('Укажите действие: '))
        flag = False
        while command != 6:
            if command == 0:
                print_help()
            elif command == 1:
                print(get_class_list())
            elif command == 2:
                get_pupils_list()
            elif command == 3:
                get_subjects()
            elif command == 4:
                get_parents_names()
            elif command == 5:
                get_class_teachers()
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

