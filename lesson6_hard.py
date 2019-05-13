__author__ = 'Смелова Анна Алексеевна'

# hard

print()
print('hard: Задание-1')
print()

# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os


class Worker():
    def __init__(self, name, surname, position, zp, n_hours, f_hours=0, salary=0):
        self.name = name
        self.surname = surname
        self.position = position
        self.zp = zp
        self.n_hours = n_hours
        self.f_hours = f_hours
        self.salary = salary

    def calc_salary(self):
        if self.f_hours != 0:
            if self.n_hours > self.f_hours: # недоработка
                self.salary = self.f_hours * self.zp / self.n_hours
            elif self.n_hours == self.f_hours: # норма
                self.salary = self.zp
            elif self.n_hours < self.f_hours: # переработка
                self.salary = self.zp + (self.f_hours - self.n_hours) * 2 * self.zp / self.n_hours
        self.salary = round(self.salary,2)


current_dir = os.getcwd()
path = os.path.join(current_dir,'lesson6_data','workers.txt')
path2 = os.path.join(current_dir,'lesson6_data','hours_of.txt')
f = open(path, 'r', encoding='UTF-8')
workers = []
for line in f:
    l = line.split()
    if l[2].isnumeric() and l[4].isnumeric():
        worker = Worker(l[0], l[1], l[3], int(l[2]), int(l[4]))
        workers.append(worker)
f.close()

f2 = open(path2, 'r', encoding='UTF-8')
for line in f2:
    l = line.split()
    for el in workers:
        if el.name == l[0] and el.surname == l[1]:
            el.f_hours = int(l[2])
            el.calc_salary()
            break
f2.close()

print('Имя Фамилия Заработная плата')
for el in workers:
    print(el.name+' '+el.surname+' '+str(el.salary))
