__author__ = 'Смелова Анна Алексеевна'

'''
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
'''

import random


class LotoTicket:
    def __init__(self):
        self.nums = LotoTicket.get_nums(random.sample(range(1,91), 15))
        self.kol = 15

    @staticmethod
    def get_nums(nums):
        line_1 = nums[0:5]
        line_1.sort()
        line_2 = nums[5:10]
        line_2.sort()
        line_3 = nums[10:]
        line_3.sort()

        result = []
        sp_l = LotoTicket.get_spaces(12)
        for k in range(5):
            result.append(str(line_1[k]).rjust(2, ' '))
            result.append(sp_l[k])
            result.append(' ')
        sp_l = LotoTicket.get_spaces(12)
        for k in range(5):
            result.append(str(line_2[k]).rjust(2, ' '))
            result.append(sp_l[k])
            result.append(' ')
        sp_l = LotoTicket.get_spaces(12)
        for k in range(5):
            result.append(str(line_3[k]).rjust(2, ' '))
            result.append(sp_l[k])
            result.append(' ')

        return result

    @staticmethod
    def get_spaces(kol):
        sp_list = []
        for i in range(4):
            num = 3 * random.randint(0, kol / 3)
            sp_list.append(' ' * num)
            kol = kol - num
        random.shuffle(sp_list)
        sp_list.append('')
        return sp_list

    def cross_out_num(self, num):
        if num in self.nums:
            i = self.nums.index(num)
            self.nums[i] = ' -'
            self.kol -= 1
            return True
        else:
            return False

    def check_winner(self):
        if self.kol == 0:
            return True
        else:
            return False


    def __str__(self):
        line_1 = self.nums[0:15]
        line_2 = self.nums[15:30]
        line_3 = self.nums[30:]

        result = ''.join(map(str, line_1)) + '\n' + ''.join(map(str, line_2)) + '\n' + ''.join(map(str, line_3))
        result += '\n' + '--------------------------'

        return result


class Pocket:
    def __init__(self):
        self.nums = random.sample(range(1,91), 90)

    def get_next(self):
        if self.nums:
            next_keg = self.nums.pop()
            print(f'Новый бочонок: {next_keg} (осталось {len(self.nums)})')
            return next_keg
        else:
            return 0

    def __str__(self):
        return str(len(self.nums)) + ':' + str(self.nums)

def print_tickets(first, second):
    print('------ Ваша карточка -----')
    print(first)
    print('-- Карточка компьютера ---')
    print(second)


print('Игра Лото')
flag = True
while flag:
    pocket = Pocket()
    hum_ticket = LotoTicket()
    comp_ticket = LotoTicket()
    print_tickets(hum_ticket, comp_ticket)

    ans = input('Начнем? (y/n) ')
    if ans == 'y':
        flag = False
        pocket_flag = True
        while pocket_flag:
            curr_keg = str(pocket.get_next()).rjust(2, ' ')
            if curr_keg != 0:
                print_tickets(hum_ticket, comp_ticket)
                comp_ticket.cross_out_num(curr_keg)
                ans = input('Зачеркнуть цифру? (y/n) ')
                if ans == 'y':
                    res = hum_ticket.cross_out_num(curr_keg)
                    if res:  # цифра есть - зачеркнули
                        pocket_flag = True
                    else:  # цифры нет - зачеркнули
                        print('Такого числа нет в вашей карточке. Игра завершена. Вы проиграли.')
                        pocket_flag = False
                else:
                    res = hum_ticket.cross_out_num(curr_keg)
                    if res:  # цифра есть - выбрали продолжить
                        print('Такое число есть в вашей карточке. Надо было зачеркнуть. Игра завершена. Вы проиграли.')
                        pocket_flag = False
                    else:  # цифры нет - выбрали продолжить
                        pocket_flag = True
                if hum_ticket.check_winner():
                    print('Игра завершена. Поздравляем! Вы выиграли!')
                    pocket_flag = False
                    if comp_ticket.check_winner():
                        print('Компьютер тоже выиграл!')
                elif comp_ticket.check_winner():
                    print('Игра завершена. Компьютер выиграл!')
                    pocket_flag = False
            else:
                print('Бочонков больше не осталось. Игра завершена.')
                pocket_flag = False

    else:
        flag = True
        print('Генерируем новые карточки...')




