__author__ = 'Смелова Анна Алексеевна'

'''
Написать реализацию игры крестики-нолики, используя принципы ООП
'''

import copy
import random

class BadValueException(Exception):
    def __init__(self, val_list):
        Exception.__init__()
        self.val_list = val_list

    def __str__(self):
        print(f'Укажите число из списка {self.val_list}: ')

class Player:
    def __init__(self, name, val):
        self.name = name
        self.val = val
        self.pos = 0

    def set_val(self, unit):
        self.pos = self.get_pos(unit)
        unit.set_field(self.pos, self.val)
        self.pos = 0


class Human(Player):
    def get_pos(self, unit):
        while True:
            try:
                pos = int(input(f'Укажите ячейку [{",".join(map(str, unit.empty_fields))}]: '))
                if not pos in unit.empty_fields:
                    raise BadValueException([])
                self.pos = pos
                break
            except:
                print('Укажите число из списка незанятых ячеек.')
        return self.pos


class Computer(Player):
    def get_pos(self, unit):
        lng = len(unit.empty_fields)
        if lng == 9:
            ind = random.randint(0, 4)
            p = [1, 3, 5, 7, 9]
            self.pos = p[ind]
        elif lng == 8:
            enemy_val = 'X'
            mas = [0, 2, 6, 8]
            if unit.board[4] == enemy_val:
                ind = random.randint(0,3)
                self.pos = mas[ind] + 1
            else:
                for m in mas:
                    if unit.board[m] == enemy_val:
                        self.pos = 5
                        break
                if self.pos != 5:
                    ind = random.randint(0,7)
                    self.pos = unit.empty_fields[ind]
        elif lng == 7:
            p = [1, 3, 7, 9]
            for k in p:
                if k in unit.empty_fields:
                    self.pos = k
                    break
        elif lng == 6:
            enemy_val = 'X'
            if unit.board[4] == self.val:
                if unit.board[0] == enemy_val and unit.board[2] == enemy_val:
                    self.pos = 2
                if unit.board[2] == enemy_val and unit.board[8] == enemy_val:
                    self.pos = 6
                if unit.board[8] == enemy_val and unit.board[6] == enemy_val:
                    self.pos = 8
                if unit.board[6] == enemy_val and unit.board[0] == enemy_val:
                    self.pos = 4
                if unit.board[0] == enemy_val and unit.board[8] == enemy_val:
                    ind = random.randint(0, 3)
                    p = [2, 4, 6, 8]
                    self.pos = p[ind]
                if unit.board[2] == enemy_val and unit.board[6] == enemy_val:
                    ind = random.randint(0, 3)
                    p = [2, 4, 6, 8]
                    self.pos = p[ind]
            else:
                self.find_pos(unit, self.val, {})

        else:
            self.find_pos(unit, self.val, {})
        return self.pos

    def find_pos(self, unit, val, steps={}, step=[], first_step_win=0, first_step_lose=0):
        enemy_val = 'X' if val == 'O' else 'O'
        hum_val = 'X' if self.val == 'O' else 'O'
        check_unit = copy.deepcopy(unit)
        if check_unit.check_win(self.val):  # если уже победили
            return 10
        elif check_unit.check_win(hum_val):  # если уже проиграли
            return -10
        elif not check_unit.empty_fields:  # если уже ничья
            return 0
        else:  # если еще есть пустые клетки
            for ef in check_unit.empty_fields:
                step.append(ef)
                check_check_unit = copy.deepcopy(check_unit)
                check_check_unit.set_field(ef, val)
                result = self.find_pos(check_check_unit, enemy_val,steps,step)
                steps[''.join(map(str, step))] = result
                step.remove(ef)
            a = {}

            for k in steps.keys():
                if int(k[0]) in game.empty_fields:
                #if int(k[0]) in unit.empty_fields:
                    if len(k) == 1 and steps[k] == 10:  # выигрыш с одного хода
                        first_step_win = int(k)
                    if len(k) == 2 and steps[k] == -10: # проигрыш с одного хода
                        first_step_lose = int(k[1])
                    if k[0] in a.keys():
                        a[k[0]] += steps[k] / len(k)
                    else:
                        a[k[0]] = steps[k] / len(k)
            if first_step_win:
                self.pos = first_step_win
            elif first_step_lose:
                self.pos = first_step_lose
            else:
                best_score = max(a.values())
                for key, value in a.items():
                    if value == best_score:
                        self.pos = int(key)
            return 0  # в неопределенной ситуации возвращаем 0


class Game:
    def __init__(self, players):
        self.board = ['1','2','3','4','5','6','7','8','9']
        self.players = players
        self.winners = {'X' : False, 'O' : False}
        self.empty_fields = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def set_field(self, pos, val):
        self.board[pos - 1] = val
        self.empty_fields.remove(pos)
        return self.board

    def check_win(self, val):
        coord = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for el in coord:
            if self.board[el[0]] == self.board[el[1]] == self.board[el[2]] == val:
                self.winners[val] = True
                return True
        return False

    def __str__(self):
        a = []
        a.append('|‾‾‾|‾‾‾|‾‾‾|\n')
        for i in self.board[:3]:
            a.append(f'| {i} ')
        a.append('|\n|___|___|___|\n|‾‾‾|‾‾‾|‾‾‾|\n')
        for i in self.board[3:6]:
            a.append(f'| {i} ')
        a.append('|\n|___|___|___|\n|‾‾‾|‾‾‾|‾‾‾|\n')
        for i in self.board[6:]:
            a.append(f'| {i} ')
        a.append('|\n|___|___|___|')
        return ''.join(map(str, a))

    def main(self):
        for i in self.players.values():
            print(self)
            if not self.empty_fields:
                print(f'Игра закончена! Ничья!')
                k = True
                return k
            print(f'Ход игрока {i.name} ({i.val})')
            i.set_val(self)
            k = self.check_win(i.val)
            if k:
                for m in self.winners.keys():
                    if game.winners[m]:
                        val = m
                        win = game.players[m].name
                print(self)
                print(f'Игра закончена! Победитель {win} ({val})!')
                break
        return k


def print_menu():
    print('Игра крестики-нолики')
    print()
    print('1. Человек - Человек')
    print('2. Человек - Компьютер')
    print('3. Компьютер - Компьютер')
    print('4. Завершить игру')
    print()

def get_name(player):
    while True:
        try:
            name = input(f'Укажите имя {player} игрока: ')
            if not name:
                raise BadValueException([])
            break
        except:
            print('Имя должно быть непустым.')
    return name

def get_role(player):
    while True:
        try:
            role = int(input(f'За кого будет играть {player}? 1 - крестики, 2 - нолики '))
            if not role in [1, 2]:
                raise BadValueException([1, 2])
            break
        except:
            print('Укажите число 1, если за крестики, и число 2, если за нолики.')
    return role

print_menu()
while True:
    try:
        type = int(input(f'Выберите тип игры 1, 2 или 3: '))
        if not type in [1, 2, 3, 4]:
            raise BadValueException([1, 2, 3, 4])
        break
    except:
        print('Укажите число 1, 2 или 3 для игры и 4 для выхода из игры.')
if type == 1:
    name_1 = get_name('первого')
    role_1 = get_role(name_1)
    name_2 = get_name('второго')
    if role_1 == 1:
        pl1 = Human(name_1, 'X')
        pl2 = Human(name_2, 'O')
    elif role_1 == 2:
        pl1 = Human(name_2, 'X')
        pl2 = Human(name_1, 'O')
    game = Game({'X': pl1, 'O': pl2})
    k = False
    while not k:
        k = game.main()
elif type == 2:
    name_1 = get_name('')
    role_1 = get_role(name_1)
    if role_1 == 1:
        pl1 = Human(name_1, 'X')
        pl2 = Computer('Computer', 'O')
    elif role_1 == 2:
        pl1 = Computer('Computer', 'X')
        pl2 = Human(name_1, 'O')
    game = Game({'X': pl1, 'O': pl2})
    k = False
    while not k:
        k = game.main()
elif type == 3:
    pl1 = Computer('Computer1', 'X')
    pl2 = Computer('Computer2', 'O')
    game = Game({'X': pl1, 'O': pl2})
    k = False
    while not k:
        k = game.main()

