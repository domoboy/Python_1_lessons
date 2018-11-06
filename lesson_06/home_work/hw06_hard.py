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


# class Workers:
#
#     def __init__(self, name, surname, position, wage, hour_rate, worked_out):
#         self.name = name  # имя сотрудника
#         self.surname = surname # фамилия сотрудника
#         self.position = position  # должность
#         self.wage = wage  # заработная плата
#         self.hour_rate = hour_rate  # норма часов
#         self.worked_out = worked_out  # отработано часов
#
#     def list_pay(self):

import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))  # меняю рабочую директорию на ту, где лежит файл


class Worker:
    def __init__(self, stringFromFile):
        elems = stringFromFile.split()
        print(elems)
        self.name = elems[0]  # имя сотрудника
        self.surname = elems[1]  # фамилия сотрудника
        self.position = elems[3]  # должность
        self.wage = int(elems[2])  # заработная плата
        self.hour_rate = int(elems[4])  # норма часов
        self.worked_out = 0
        self.payment = 0

    def calc_pay(self, worked_out):
        self.worked_out = worked_out
        h_pay = int(self.wage / self.hour_rate)

        if worked_out == self.hour_rate:
            self.payment = self.wage
        elif worked_out > self.hour_rate:
            self.payment = self.wage + (worked_out - self.hour_rate) * h_pay * 2
        else:
            self.payment = worked_out * h_pay

        return self.payment

    def dump(self):
        print(self.surname, self.name, self.worked_out, self.payment)


personal = []

with open('data/workers', encoding='UTF-8') as lister:
    i = 0
    for string in lister:
        if i == 0:
            i += 1
            continue

        pers = Worker(string)

        personal.append(pers)
        i += 1


def tolist(path):
    with open(path, encoding='UTF-8') as lister:
        nlist = [elems for elems in lister]
        nlist = [[el.strip() for el in elem if len(el)] for
                 elem in [elems.split(' ') for elems in nlist]]
        return nlist


hours_of = tolist('data/hours_of')

for i, data in enumerate(hours_of):
    if i == 0: continue
    p = list(filter(lambda x: x.name == data[0] and x.surname == data[1], personal))[0]

    p.calc_pay(int(data[2]))
    p.dump()

# осталось причесать.
