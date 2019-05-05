__author__ = 'Смелова Анна Алексеевна'

# easy

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

print('easy: Задание-1')
print()

import random

random_list = [random.randint(-10,10) for _ in range(10)]
print('Исходный произвольный список:')
print(random_list)
new_list = [el ** 2 for el in random_list]
print('Новый список:')
print(new_list)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

print()
print('easy: Задание-2')
print()

fruit_list_1 = ['апельсин', 'мандарин', 'яблоко', 'лимон', 'киви', 'яблоко', 'грейпфрукт']
print('Список 1:')
print(fruit_list_1)
fruit_list_2 = ['яблоко','манго','апельсин','ананас', 'грейпфрукт', 'яблоко']
print('Список 2:')
print(fruit_list_2)

common_list = list(set([el for el in fruit_list_1 if el in fruit_list_2]))
print('Фрукты в пересечении: ')
print(common_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

print()
print('easy: Задание-3')
print()

import random

random_list = [random.randint(-10, 10) for _ in range(100)]
new_list = [el for el in random_list if el % 3 == 0 and el > 0 and el % 4 != 0]
print('Исходный список:')
print(random_list)
print('Модифицированный список:')
print(new_list)


# normal

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

print()
print('normal: Задание-1')
print()

import re

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

# Решение с помощью модуля re
pattern = r'[A-Z]+'
result = re.split(pattern,line)
print('Результат с помощью модуля re: ')
print(result)

# Решение без помощи модуля re
result_2 = []
elem = ''
for el in line:
    if el.islower():
        elem = elem + el
    else:
        if elem:
            result_2.append(elem)
        elem = ''
print('Результат без помощи модуля re: ')
print(result_2)


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

print()
print('normal: Задание-2')
print()

import re

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

# Решение с помощью модуля re
#line = 'GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec'
pattern = r'[a-z]{2}([A-Z]+)[A-Z]{2}'
result = re.findall(pattern,line_2)
print('Результат с помощью модуля re: ')
print(result)

# Решение без помощи модуля re
result_2 = []
elem = ''
low_kol = 0
up_kol = 0
start = False
finish = False
for s in line_2:
    if s.islower():
        if start:
            start = False
            if up_kol > 2:
                result_2.append(elem[:-2])
            up_kol = 0
            elem = ''
        low_kol = low_kol + 1
        if low_kol >= 2:
            start = True
    if s.isupper():
        low_kol = 0
        if start:
            up_kol = up_kol + 1
            elem = elem + s
print('Результат без помощи модуля re: ')
print(result_2)


# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

print()
print('normal: Задание-3')
print()

import random
import re
# сначала заполняем файл
f = open('task_3_normal.txt', 'w')
random_number = ''
for _ in range(2500):
    random_number = random_number + str(random.randint(0,9))
f.write(random_number)
f.close()

# теперь открываем его на чтение
f = open('task_3_normal.txt', 'r')
line = f.read()
a = {}

# функция, которая заполняет словарь a значениями длин самых длинных последовательностей цифр
# возвращает заполненный словарь
def get_seq_num(num, line):
    pattern = str(num) + '+'
    res = re.findall(pattern, line)
    a[num] = max(list(map(len, res)))
    return a

# идем по всем элементам a и строим самые длинные последовательности одинаковых цифр
for k in range(10):
    a = get_seq_num(k, line)
max_len = max(a.values())
for el in a.items():
    if el[1] == max_len:
        res = ''
        for _ in range(max_len):
            res = res + str(el[0])
        print('Самая длинная последовательность одинаковых цифр в файле: ' + str(res))
f.close()

# hard

# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:

matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2],
          [1, 1, 1]]

# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку

print()
print('hard: Задание-1')
print()

# Решение 1 (как на уроке)
print('matrix_rotate = ', list(map(list, zip(*matrix))))
# Решение 2 (чуть длиннее, но тоже в одну строку)
print('matrix_rotate = ', [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))])


# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:

print()
print('hard: Задание-2')
print()

import regex

number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

# шаблон - 5 подряд идущих цифр
pattern = r'\d{5}'
# используем regex, т.к. он умеет искать по пересекающимся шаблонам
fifths = regex.findall(pattern, number, overlapped=True) # выбрали все подряд идущие пятерки
# ищем произведения цифр в пятерках и записываем их в список mult
mult = []
for el in fifths:
    pr = 1
    for s in el:
        pr = pr * int(s)
    mult.append(pr)

max_pr = max(mult) # наибольшее произведение
# индекс смещения первой цифры пятерки совпадает с индексом наибольшего произведения в списке mult
ind = mult.index(max_pr)

print(f'Произведение: {max_pr}')
print(f'Индекс смещения первой цифры пятерки: {ind}')


# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

#[1,7] [2,4] [3,2] [4,8] [5,6] [6,1] [7,3] [8,5] - координаты когда не бьют

print()
print('hard: Задание-3')
print()

# Функция возвращает список координат полей, которые находятся под атакой
def get_fields_under_attack(x_pos, y_pos):
    result = []
    for i in range(8):
        if i != y_pos:
            # добавляем все координаты по горизонтали за исключением отправной точки
            result.append([x_pos, i])
        if i != x_pos:
            # добавляем все координаты по вертикали за исключением отправной точки
            result.append([i, y_pos])
    # далее добавляем все координаты по диагонали за исключением отправной точки
    j = 1
    while x_pos - j > 0 and y_pos - j > 0:
        result.append([x_pos - j, y_pos - j])
        j = j + 1
    j = 1
    while x_pos - j > 0 and y_pos + j < 7:
        result.append([x_pos - j, y_pos + j])
        j = j + 1
    j = 1
    while x_pos + j < 7 and y_pos - j > 0:
        result.append([x_pos + j, y_pos - j])
        j = j + 1
    j = 1
    while x_pos + j < 7 and y_pos + j < 7:
        result.append([x_pos + j, y_pos + j])
        j = j + 1
    return result

# Функция заполняет шахматное поле метками:
# 1 - стоит ферзь
# 2 - поле под атакой
# 3 - стоит ферзь под атакой
# flag - показатель того, что есть ферзи, которые бьют друг друга
# Функция возвращает шахматное поле и флаг атаки
def fill_board(chess_board, x, y, flag):
    chess_board[x - 1][y - 1] = 1
    for k in get_fields_under_attack(x - 1, y - 1):
        if chess_board[k[0]][k[1]] != 1 and chess_board[k[0]][k[1]] != 3:
            chess_board[k[0]][k[1]] = 2
        else:
            flag = True
            chess_board[k[0]][k[1]] = 3
    return [chess_board, flag]

# определяем шахматное поле и заполняем его нулями
chess_board = [[0 for _ in range(8)] for _ in range(8)]

# флаг атаки
b_under_attack = False

# Определяем класс ошибки, чтобы отлавливать неправильно введенные данные
class ValueIntervalException(Exception):
    pass
# Определяем класс ошибки, чтобы отлавливать уже занятые поля
class BusyFieldException(Exception):
    pass

# Функция получает координаты от пользователя и делает все необходимые проверки
def get_coord(chess_board, b_under_attack, num):
    while True:
        try:
            x, y = map(int, input(f'Укажите координаты {num} ферзя через пробел: ').split())
            if not 1 <= x <= 8 or not 1 <= y <= 8:
                raise ValueIntervalException
            if chess_board[x - 1][y - 1] == 1 or chess_board[x - 1][y - 1] == 3:
                raise BusyFieldException
        except ValueError:
            print('Координаты должны быть целыми числами.')
        except ValueIntervalException:
            print('Координаты должны быть целыми числами в диапазоне от 1 до 8.')
        except BusyFieldException:
            print('Данные координаты уже заняты ферзем. Укажите другие координаты.')
        else:
            res = fill_board(chess_board, x, y, b_under_attack)
            chess_board = res[0]
            b_under_attack = res[1]
            break
    return [chess_board, b_under_attack]

# запрашиваем координаты ферзей у пользователя
for num in range(8):
    res = get_coord(chess_board, b_under_attack, num + 1)
    chess_board = res[0]
    b_under_attack = res[1]

if b_under_attack:
    print('YES')
else:
    print('NO')
