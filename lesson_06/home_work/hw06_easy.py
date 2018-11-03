# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Triangle:

    def __init__(self, coord_ax, coord_ay, coord_bx, coord_by, coord_cx, coord_cy):
        self.coord_ax = coord_ax
        self.coord_ay = coord_ay
        self.coord_bx = coord_bx
        self.coord_by = coord_by
        self.coord_cx = coord_cx
        self.coord_cy = coord_cy

    def sides_triangle(self):  # формула расчета длины стороны треугольника TODO оптимизировать

        sides = {}

        sides[0] = math.sqrt(((int(self.coord_bx) - int(self.coord_ax)) ** 2) + ((int(self.coord_by) -\
                                                                                  int(self.coord_ay)) ** 2))
        sides[1] = math.sqrt(((int(self.coord_cx) - int(self.coord_ax)) ** 2) + ((int(self.coord_cy) -\
                                                                                  int(self.coord_ay)) ** 2))
        sides[2] = math.sqrt(((int(self.coord_cx) - int(self.coord_bx)) ** 2) + ((int(self.coord_cy) -\
                                                                                  int(self.coord_by)) ** 2))

        return sides

    def area_triangle(self):  # формула расчета площади треугольника (формула Герона)

        pp = (self.perimeter_triangle()) / 2  # полупериметр

        area = math.sqrt(pp * (pp - self.sides_triangle()[0]) * (pp - self.sides_triangle()[1]) *\
                         (pp - self.sides_triangle()[2]))

        return area

    def triangle_height(self):  # формула рачета высоты треугольника. TODO Оптимизировать

        tr_height = {}

        tr_height[0] = (self.area_triangle() * 2) / self.sides_triangle()[2]

        tr_height[1] = (self.area_triangle() * 2) / self.sides_triangle()[1]

        tr_height[2] = (self.area_triangle() * 2) / self.sides_triangle()[0]

        return tr_height

    def perimeter_triangle(self):  # формула расчета периметра треугольника

        perimeter = self.sides_triangle()[0] + self.sides_triangle()[1] + self.sides_triangle()[2]

        return perimeter


triangle = Triangle('3', '3', '4', '6', '7', '2')

print(triangle.sides_triangle())  # длины сторон
print(triangle.area_triangle())  # площадь треугольника
print(triangle.triangle_height())  # высоты треугольника ha, hb, hc
print(triangle.perimeter_triangle())  # периметр треугольника

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

'''
равнобочная (равнобокая) трапеция - трапеция у которой боковые стороны равны
'''


class Trapezium:

    def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.dx = dx
        self.dy = dy

    def tru_trap(self):
        if self.sid_trap()[0] == self.sid_trap()[2]:
            tr = self.sid_trap()[0]
            return tr
        else:
            print("Увы, это не равнобочная трапеция, боковые стороны не равны друг другу")

    def sid_trap(self):  # длина сторон

        sides = {}

        sides[0] = math.sqrt(((int(self.bx) - int(self.ax)) ** 2) + ((int(self.by) - int(self.ay)) ** 2))
        sides[1] = math.sqrt(((int(self.cx) - int(self.bx)) ** 2) + ((int(self.cy) - int(self.by)) ** 2))
        sides[2] = math.sqrt(((int(self.dx) - int(self.cx)) ** 2) + ((int(self.dy) - int(self.cy)) ** 2))
        sides[3] = math.sqrt(((int(self.ax) - int(self.dx)) ** 2) + ((int(self.ay) - int(self.dy)) ** 2))

        return sides

    def per_trap(self):  # периметр трапеции

        per = self.sid_trap()[0] + self.sid_trap()[1] + self.sid_trap()[2] + self.sid_trap()[3]

        return per

    def trapezoid_height(self):  # высота равнобокой трапеции

        h = math.sqrt((int(self.tru_trap() ** 2) - (((self.sid_trap()[3] - self.sid_trap()[1]) ** 2) / 4)))

        return h

    def area_trap(self):

        s = ((self.sid_trap()[1] + self.sid_trap()[3]) / 2) * self.trapezoid_height()

        return s


trapezium = Trapezium('2', '1', '3', '5', '8', '5', '9', '1')

print('Это равнобочнаятрапеция, так как ее боковые стороны равны: {}'.format(trapezium.tru_trap()))
print(trapezium.sid_trap())  # длины сторон
print(trapezium.area_trap())  # площадь трапеции
print(trapezium.trapezoid_height())  # высота трапеции
print(trapezium.per_trap())  # периметр трапеции

