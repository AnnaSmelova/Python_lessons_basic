__author__ = 'Смелова Анна Алексеевна'

#easy

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# Решение 1
def my_round(number, ndigits):
    str_number = str(number)
    dot = str_number.index('.')
    if dot != -1:
        dec = str_number[dot + 1:] # дробная часть числа
        num = str_number[:dot] # целая часть числа
        if len(dec) <= ndigits:
            return number
        else:
            if int(dec[dot + ndigits - 1]) < 5:
                # если округлять не надо - просто обрезаем дробную часть
                return float(str_number[:dot + ndigits + 1])
            else:
                # округляем
                end = int(str_number[dot + ndigits]) + 1
                if end == 10:
                    while end == 10 and ndigits > 1:
                        ndigits = ndigits - 1
                        end = int(str_number[dot + ndigits]) + 1
                    if end == 10:
                        num = int(num) + 1
                        end = 0
                return float(str(num) + str_number[dot:dot + ndigits] + str(end))
    else:
        return number

# Решение 2
def my_round2(number, ndigits):
    lng = len(str(int(number))) + 1 + ndigits # длина целой части + '.' + кол-во знаков после точки
    for k in range(ndigits):
        number = number * 10
    num = int(number * 10)
    end = num % 10
    if end >= 5:
        number = int(number) + 1
    else:
        number = int(number)
    for m in range(ndigits):
        number = number / 10
    string = '{:.' + str(lng) + '}'
    return string.format(str(number))


a = float(input('Укажите десятичное число: '))
b = int(input('Укажите количество знаков после запятой: '))
print('Результат округления my_round: ' + str(my_round(a, b)))
print('Результат округления my_round2: ' + str(my_round(a, b)))
print('Результат округления встроенной функцией round для проверки: ' + str(round(a, b))) # для проверки

#print(my_round(1.1234567, 5))
#print(my_round(2.1999967, 5))
#print(my_round(2.9999967, 5))



# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    if not ticket_number.isnumeric():
        return 'Номер билета должен быть целым положительным числом'
    str_number = str(ticket_number)
    lng = len(str_number)
    if lng % 2 != 0:
        return 'Нельзя определить, т.к. нечетное количество цифр'
    else:
        ln = int(lng / 2)
        first_part = str_number[:ln]
        first_sum = 0
        second_part = str_number[ln:]
        second_sum = 0
        for k in range(ln):
            first_sum = first_sum + int(first_part[k])
            second_sum = second_sum + int(second_part[k])
        if first_sum == second_sum:
            return 'Счастливый билет :)'
        else:
            return 'Несчастливый билет :('


ticket_number = input('Укажите номер билета: ')
print(lucky_ticket(ticket_number))



#normal

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    if n > m:
        return []
    else:
        if n <= 0:
            n = 1
        if m <= 0:
            m = 1
        if m == 1:
            return [1]
        elif m == 2:
            if n == m:
                return [1]
            return [1, 1]
        else:
            a = 1
            b = 1
            for i in range(n - 1):
                result = a + b
                a = b
                b = result
            j = n
            mass = []
            while j <= m:
                mass.append(a)
                result = a + b
                a = b
                b = result
                j = j + 1
            return mass

n, m = map(int, input('Укажите начало и конец ряда Фибоначчи: ').split())
print(fibonacci(n, m))



# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    lng = len(origin_list)
    while lng > 0:
        for i in range(lng):
            if origin_list[i] % 1 == 0:
                origin_list[i] = int(origin_list[i]) # для красоты обратно в int переведем
            if i < lng - 1:
                if origin_list[i] > origin_list[i + 1]:
                    temp = origin_list[i]
                    origin_list[i] = origin_list[i + 1]
                    origin_list[i + 1] = temp
        lng = lng - 1
    return origin_list


#print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
origin_list = list(map(float, input('Укажите элементы списка через пробел: ').split()))
print(sort_to_max(origin_list))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, orig_list):
    result_list = []
    for k in orig_list:
        if func(k):
            result_list.append(k)
    return result_list

#orig_list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
orig_list = list(map(int, input('Укажите элементы списка через пробел: ').split()))
print('Список, отсортированный my_filter: ' + str(my_filter(lambda x: x % 5 == 0, orig_list)))
print('Результат работы функции filter для проверки: ' + str(list(filter(lambda x: x % 5 == 0, orig_list))))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# Функция проверяет, является ли именно четырёхугольник А1А2А3А4 параллелограммом
# Ищем координаты середин диагоналей A1A3 и A2A4
# Если они совпадают, значит четырехуголник - параллелограмм
def check_par_1(a1,a2,a3,a4):
    # если хотя бы две точки совпадают, то это не параллелограмм
    if a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 or a2 == a4 or a3 == a4:
        return 0
    # ищем середины диагоналей
    s1x = (a1[0] + a3[0]) / 2
    s1y = (a1[1] + a3[1]) / 2
    s2x = (a2[0] + a4[0]) / 2
    s2y = (a2[1] + a4[1]) / 2

    if s1x == s2x and s1y == s2y:
        return 1
    else:
        return 0

# Функция проверяет, не схлопывается ли паралеллограмм в одну прямую линию
# Для этого вычисляем косинус угла между тремя точками по координатам
def check_line(a1,a2,a3):
    ch = ((a1[0] - a2[0]) * (a3[0] - a2[0]) + (a1[1] - a2[1]) * (a3[1] - a2[1]))
    zn = (((a1[0]-a2[0])**2 + (a1[1]-a2[1])**2)**0.5) * (((a3[0]-a2[0])**2 + (a3[1]-a2[1])**2)**0.5)
    cos_k = ch / zn
    if round(cos_k,1) == 1:
        return 0
    else:
        return 1

# Функция ищет среди данных точек цикл, который будет параллелограммом
# Все циклы разбиваются на три случая:
# A1А2А3А4 = А4А1А2А3 = 3412 = 2341 = 4321 = 1432 = 2143 = 3214
# А1А3А2А4 = А4А1А3А2 = 2413 = 3241 = 4231 = 1423 = 3142 = 2314
# А1А3А4А2 = А2А1А3А4 = 4213 = 3421 = 2431 = 1243 = 3124 = 4312
# Для проверки каждого цикла используется функция check_par_1
# При этом еще проверяем, не схлопывается ли паралелограмм в одну линию функцией check_line
# Пример, когда схлопывается А1(1,2),А2(2,4),А3(5,6),А4(7,8)
def check_par(a1,a2,a3,a4):
    is_par = False
    if check_par_1(a1,a2,a3,a4):
        if check_line(a1,a2,a3) and check_line(a2,a1,a4):
            is_par = True
            cycle = 'A1A2A3A4'
    elif check_par_1(a1,a3,a2,a4):
        if check_line(a1, a3, a2) and check_line(a3, a1, a4):
            is_par = True
            cycle = 'A1A3A2A4'
    elif check_par_1(a1,a3,a4,a2):
        if check_line(a1, a3, a4) and check_line(a3, a1, a2):
            is_par = True
            cycle = 'A1A3A4A2'
    if is_par:
        return cycle
    else:
        return 0

a1 = list(map(int, input('Укажите координаты точки А1 через пробел: ').split()))
a2 = list(map(int, input('Укажите координаты точки А2 через пробел: ').split()))
a3 = list(map(int, input('Укажите координаты точки А3 через пробел: ').split()))
a4 = list(map(int, input('Укажите координаты точки А4 через пробел: ').split()))

result = check_par(a1,a2,a3,a4)
if not result:
    print('Точки А1, А2, А3, А4 не являются вершинами параллелограмма')
else:
    print('Четырехугольник ' + str(result) + ' - параллелограмм')


#hard

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

import math

eq = input('Укажите выражение: ').split()
lng = len(eq)
# op - глобальный знак всей операции
if '+' in eq:
    pos = eq.index('+')
    op = 1
else:
    pos = eq.index('-')
    op = -1

if pos == 1:
    if '/' in eq[0]:
        wh_1 = 0
        dec_1 = list(map(int, eq[0].split('/')))
        op_1 = 1
        if dec_1[0] < 0:
            op_1 = -1
            dec_1[0] = (-1) * dec_1[0]
    else:
        wh_1 = int(eq[0])
        op_1 = 1
        if wh_1 < 0:
            op_1 = -1
            wh_1 = (-1) * wh_1
        dec_1 = [wh_1, 1]

elif pos == 2:
    wh_1 = int(eq[0])
    op_1 = 1
    if wh_1 < 0:
        op_1 = -1
        wh_1 = (-1) * wh_1
    dec_1 = list(map(int, eq[1].split('/')))
    dec_1[0] = dec_1[0] + wh_1 * dec_1[1]
if pos + 1 == lng - 1:
    if '/' in eq[pos + 1]:
        wh_2 = 0
        dec_2 = list(map(int, eq[pos + 1].split('/')))
        op_2 = 1
        if dec_2[0] < 0:
            op_2 = -1
            dec_2[0] = (-1) * dec_2[0]
    else:
        wh_2 = int(eq[pos + 1])
        op_2 = 1
        if wh_2 < 0:
            op_2 = -1
            wh_2 = (-1) * wh_2
        dec_2 = [wh_2, 1]
elif pos + 1 == lng - 2:
    wh_2 = int(eq[pos + 1])
    op_2 = 1
    if wh_2 < 0:
        op_2 = -1
        wh_2 = (-1) * wh_2
    dec_2 = list(map(int, eq[pos + 2].split('/')))
    dec_2[0] = dec_2[0] + wh_2 * dec_2[1]

res_ch = op_1 * dec_1[0] * dec_2[1] + op * op_2 * dec_2[0] * dec_1[1]
res_zn = dec_1[1] * dec_2[1]

res_op = 1
if res_ch < 0:
    res_op = -1
    res_ch = (-1) * res_ch

whole_part = res_op * (res_ch // res_zn)
part_part = res_ch % res_zn
k = math.gcd(part_part,res_zn)
part_part = int(part_part / k)
res_zn = int(res_zn / k)

if whole_part == 0:
    whole_part = ''
    if part_part == 0:
        whole_part = '0'
else:
    whole_part = str(whole_part) + ' '
if part_part == 0:
    part_part = ''
else:
    part_part = str(part_part) + '/' + str(res_zn)


result = whole_part + part_part

print(result)



# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# Не хватило времени. Пришлю позже

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

# Не хватило времени. Пришлю позже

