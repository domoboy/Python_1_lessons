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


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# Python_1_lessons/lesson_03_home_work/

import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))  # меняю рабочую директорию на ту, где лежит файл


# Возвращает массив строк из файла path
def tolist(path):
    with open(path, encoding='UTF-8') as lister:
        nlist = [elems for elems in lister]
        nlist = [[el.strip() for el in elem if len(el)] for
                 elem in [elems.split(' ') for elems in nlist]]
        return nlist


# Возвращает массив словарей с ключами из header и соответсвующими им значениями из values
def couple(header, values):
    nlist = [list(zip(header, value)) for value in values]
    nlist = [{elem[0]: elem[1] for elem in elems} for elems in nlist]
    return nlist


# Возвращает общую таблицу из file1 и file2 в виде списка из словарей по каждому сотруднику
def merge(file1, file2):
    persons_list = tolist(file1)  # Создание списка строк из табл.№1
    houres_list = tolist(file2)  # Создание списка строк из табл.№2
    header_p = persons_list.pop(0)  # Выделение заголовка из табл.№1
    header_h = houres_list.pop(0)  # Выделение заголовка из табл.№2

#  Создание пары заголовок - значение для каждого сотрудника в каждой таблице
    personal = couple(header_p, persons_list)
    hourse = couple(header_h, houres_list)

#  Слияние таблиц
    for el in personal:
        for e in hourse:
            if (el['Фамилия'] == e['Фамилия'] and
               el['Имя'] == e['Имя']):
                el.update(e)

    return personal


# Расчёт зарплаты
def calc_pay(tabl):

    for person in tabl:
        pay = int(person['Зарплата'])
        h_need = int(person['Норма_часов'])
        h_fact = int(person['Отработано'])
        h_pay = int(pay / h_need)

        if h_fact == h_need:
            person['Расчёт'] = '{}'.format(pay)
        elif h_fact > h_need:
            person['Расчёт'] = '{}'.format(pay + (h_fact-h_need) * h_pay*2)
        else:
            person['Расчёт'] = '{}'.format(h_pay * h_fact)

    return tabl


personal = calc_pay(merge('data/workers', 'data/hours_of'))

with open('calc_pay', 'w', encoding='UTF-8') as pay_list:

    header = '{:<10}{:<12}{:<10}\n'.format('Имя', 'Фамилия', 'Расчёт')
    body = '\n'.join(['{:<10}{:<12}{:<10}'.format(pers['Имя'], pers['Фамилия'], pers['Расчёт']) for pers in personal])

    print(header + body)

    pay_list.write(header + body)


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

'''
Открываем файл на чтение
менеджеры контекста позволят не делать close https://pythonworld.ru/osnovy/with-as-menedzhery-konteksta.html
Перебираем фрукты и складываем их в словари ключ буква, хначение список всех соответствующих

половину подсмотрел



list_fruits = tuple(map(chr, range(ord('А'), ord('Я')+1)))


def collect_fruits(file):  # функция, которая будет собирать фрукты в словари по алфавиту
    with open(file, "r", encoding="UTF-8") as x:
        fruit = []  # Создаю пустой список, куда буду все складывать
        all_fr = [el_fruit.strip() for el_fruit in x]  # Сначала избавимся от пробелов для всех элементов фруктов
        all_fr = [el_fruit for el_fruit in all_fr if len(el_fruit)]  # если по длине проходит, то присваиваем элемент
        for letter in list_fruits:  # для букв из списка фруктов начинаем цикл
            sort_fruit = [el_fruit for el_fruit in all_fr if letter == el_fruit[0]]  # список по букве
            if len(sort_fruit):
                fruit.append({letter: sort_fruit})  # добавляем фрукты в словарь

    return fruit


def write_fruits(fruit_list):  # функция, которая будет создавать файл фруктов на определенную букву
    for el_fruit in fruit_list:
        for key, value in el_fruit.items():
            with open("fruit_" + key + ".txt", "w", encoding="UTF-8") as fr_lst_sort:

                fr_lst_sort.write("\n\n".join(value))


write_fruits(collect_fruits("lesson_03/home_work/data/fruits.txt"))

'''

# Завелось, только когда указал путь до начала папки, но и все файлы создала в корне, а не в папке data
