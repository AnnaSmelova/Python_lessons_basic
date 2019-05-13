__author__ = 'Смелова Анна Алексеевна'

# easy

print()
print('easy: Задача-1')
print()

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    # Метод, определяющий длины сторон треугольника
    # Возвращает список длин трех сторон
    def get_sides(self):

        def get_side(x1, y1, x2, y2):
            return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        a = get_side(self.x1, self.y1, self.x2, self.y2)
        b = get_side(self.x2, self.y2, self.x3, self.y3)
        c = get_side(self.x3, self.y3, self.x1, self.y1)
        return [a, b, c]

    # Метод, определяющий периметр треугольника
    # Возвращает число - периметр, округленный до 2 знаков после запятой
    def get_perimeter(self):
        sides = self.get_sides()
        return round(sum(sides),2)

    # Метод, определяющий площадь треугольника по формуле Герона
    # Возвращает число - площадь, округленная до 2 знаков после запятой
    def get_square_gerone(self):
        semi_p = self.get_perimeter() / 2
        sides = self.get_sides()
        s = (semi_p * (semi_p - sides[0]) * (semi_p - sides[1]) * (semi_p - sides[2])) ** 0.5
        return round(s,2)

    # Метод, определяющий высоты треугольника
    # Возвращает список трех высот треугольника, округленных до 2 знаков после запятой
    def get_heights(self):
        s = self.get_square_gerone()
        sides = self.get_sides()
        h_a = (2 * s) / sides[0]
        h_b = (2 * s) / sides[1]
        h_c = (2 * s) / sides[2]
        return list(map(lambda i: round(i,2), [h_a, h_b, h_c]))


tr1 = Triangle(0, 0, 0, 1, 1, 0)
sides = list(map(lambda i: round(i, 2), tr1.get_sides()))
print(f'Треугольник со сторонами {sides[0]}, {sides[1]}, {sides[2]}')
print(f'Площадь = {tr1.get_square_gerone()}')
print(f'Высота = {tr1.get_heights()[0]}')
print(f'Периметр = {tr1.get_perimeter()}')
print()
tr2 = Triangle(-5, 0, 0, 1, 1, 0)
sides = list(map(lambda i: round(i, 2), tr2.get_sides()))
print(f'Треугольник со сторонами {sides[0]}, {sides[1]}, {sides[2]}')
print(f'Площадь = {tr2.get_square_gerone()}')
print(f'Высота = {tr2.get_heights()[0]}')
print(f'Периметр = {tr2.get_perimeter()}')

print()
print('easy: Задача-2')
print()

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapezium:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    # Метод, определяющий длины сторон трапеции
    # Возвращает список длин четырех сторон
    def get_sides(self):
        def get_side(x1, y1, x2, y2):
            return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        a = get_side(self.x1, self.y1, self.x2, self.y2)
        b = get_side(self.x2, self.y2, self.x3, self.y3)
        c = get_side(self.x3, self.y3, self.x4, self.y4)
        d = get_side(self.x4, self.y4, self.x1, self.y1)
        return [a, b, c, d]

    # Метод определяет, какие из сторон трапеции являются основаниями
    # Возвращает словарь, в котором ключами являются типы сторон
    # Значениями являются списки [тип стороны, длина, координаты первой точки, координаты второй точки]
    def get_bases(self):
        a, b, c, d = self.get_sides()

        # функция проверяет параллельность сторон по координатам
        def check_par(l1, l2):
            try:
                if (l1[4] - l1[2]) / (l1[5] - l1[3]) == (l2[4] - l2[2]) / (l2[5] - l2[3]):
                    return True
                else:
                    return False
            except ZeroDivisionError:
                if l1[5] - l1[3] == l2[5] - l2[3]:
                    return True
                elif l1[4] - l1[2] == l2[4] - l2[2] and l1[4] - l1[2] == 0:
                    return True
                else:
                    return False

        s = {'a': ['',a, self.x1, self.y1, self.x2, self.y2],
             'b': ['',b, self.x2, self.y2, self.x3, self.y3],
             'c': ['',c, self.x3, self.y3, self.x4, self.y4],
             'd': ['',d, self.x4, self.y4, self.x1, self.y1]}

        if check_par(s['a'], s['b']):
            if s['a'][1] >= s['b'][1]:
                s['a'][0] = 'b_base'
                s['b'][0] = 's_base'
            else:
                s['a'][0] = 's_base'
                s['b'][0] = 'b_base'
            s['c'][0] = 'side_1'
            s['d'][0] = 'side_2'
        elif check_par(s['b'], s['c']):
            if s['b'][1] >= s['c'][1]:
                s['b'][0] = 'b_base'
                s['c'][0] = 's_base'
            else:
                s['b'][0] = 's_base'
                s['c'][0] = 'b_base'
            s['a'][0] = 'side_1'
            s['d'][0] = 'side_2'
        elif check_par(s['c'], s['d']):
            if s['c'][1] >= s['d'][1]:
                s['c'][0] = 'b_base'
                s['d'][0] = 's_base'
            else:
                s['c'][0] = 's_base'
                s['d'][0] = 'b_base'
            s['a'][0] = 'side_1'
            s['b'][0] = 'side_2'
        elif check_par(s['d'], s['a']):
            if s['d'][1] >= s['a'][1]:
                s['d'][0] = 'b_base'
                s['a'][0] = 's_base'
            else:
                s['d'][0] = 's_base'
                s['a'][0] = 'b_base'
            s['c'][0] = 'side_1'
            s['b'][0] = 'side_2'
        elif check_par(s['a'], s['c']):
            if s['a'][1] >= s['c'][1]:
                s['a'][0] = 'b_base'
                s['c'][0] = 's_base'
            else:
                s['a'][0] = 's_base'
                s['c'][0] = 'b_base'
            s['d'][0] = 'side_1'
            s['b'][0] = 'side_2'
        elif check_par(s['b'], s['d']):
            if s['b'][1] >= s['d'][1]:
                s['b'][0] = 'b_base'
                s['d'][0] = 's_base'
            else:
                s['b'][0] = 's_base'
                s['d'][0] = 'b_base'
            s['a'][0] = 'side_1'
            s['c'][0] = 'side_2'

        dict = {}
        for i in s.values():
            dict[i[0]] = i
        return dict

    # Метод, определяющий периметр трапеции
    # Возвращает число - периметр, округленный до 2 знаков после запятой
    def get_perimeter(self):
        sides = self.get_sides()
        return round(sum(sides), 2)

    # Метод, определяющий угол между основанием и боковой стороной
    # Возвращает косинус угла
    # l1 - данные стороны основания, l2 - данные боковой стороны
    def get_angle(self, l1, l2):
        if l1[2] == l2[2] and l1[3] == l2[3]:
            x_1 = l1[4] - l1[2]
            y_1 = l1[5] - l1[3]
            x_2 = l2[4] - l2[2]
            y_2 = l2[5] - l2[3]
        elif l1[2] == l2[4] and l1[3] == l2[5]:
            x_1 = l1[4] - l1[2]
            y_1 = l1[5] - l1[3]
            x_2 = l2[2] - l2[4]
            y_2 = l2[3] - l2[5]
        elif l1[4] == l2[2] and l1[5] == l2[3]:
            x_1 = l1[2] - l1[4]
            y_1 = l1[3] - l1[5]
            x_2 = l2[4] - l2[2]
            y_2 = l2[5] - l2[3]
        else:
            print('Стороны не смежные')
            return None
        cos_a = (x_1 * x_2 + y_1 * y_2) / (((x_1 * x_1 + y_1 * y_1) * (x_2 * x_2 + y_2 * y_2)) ** 0.5)
        return cos_a

    # Метод, определяющий высоту трапеции
    # Возвращает число - высоту трапеции
    def get_height(self):
        s = self.get_bases()
        cos_a = self.get_angle(s['b_base'], s['side_1'])
        sin_a = (1 - cos_a * cos_a) ** 0.5
        if cos_a != 0:
            h = s['side_1'][1] * sin_a
        else:
            h = s['side_1'][1]
        return h

    # Метод, определяющий площадь трапеции
    # Возвращает число - площадь, округленная до 2 знаков после запятой
    def get_square(self):
        dict = self.get_bases()
        h = self.get_height()
        s = ((dict['b_base'][1] + dict['s_base'][1]) * h) / 2
        return round(s,2)

    # Метод, определяющий, является ли трапеция равнобедренной
    # Возвращает 'Да', если равнобедренная и 'Нет', если нет
    def check_isosceles(self):
        sides = self.get_sides()
        if sides[0] == sides[2] or sides[1] == sides[3]:
            return 'Да'
        else:
            return 'Нет'


tr1 = Trapezium(-4, 0, 0, 6, 4, 6, 8, 0)
sides = list(map(lambda i: round(i, 2), tr1.get_sides()))
print(f'Трапеция со сторонами {sides[0]}, {sides[1]}, {sides[2]}, {sides[3]}')
print(f'Площадь = {tr1.get_square()}')
print(f'Высота = {tr1.get_height()}')
print(f'Периметр = {tr1.get_perimeter()}')
print(f'Является ли равнобедренной: {tr1.check_isosceles()}')
print()
tr2 = Trapezium(0, 0, 0, 6, 4, 6, 8, 0)
sides = list(map(lambda i: round(i, 2), tr2.get_sides()))
print(f'Трапеция со сторонами {sides[0]}, {sides[1]}, {sides[2]}, {sides[3]}')
print(f'Площадь = {tr2.get_square()}')
print(f'Высота = {tr2.get_height()}')
print(f'Периметр = {tr2.get_perimeter()}')
print(f'Является ли равнобедренной: {tr2.check_isosceles()}')

