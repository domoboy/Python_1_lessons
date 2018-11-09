#!/usr/bin/python3

"""
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
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

from random import randint


# Класс с картами игроков
class Rulottocard:
    def __init__(self, name):
        bag = [x for x in range(1, 91)]
        # self.digits = []
        self.card = [
            __class__.gen_string(bag),
            __class__.gen_string(bag),
            __class__.gen_string(bag)
        ]
        self.name = name
        self.count_barrel = 15

# Собирается карточка игроков.
    @staticmethod
    def gen_string(bag):
        string = ['' for i in range(9)]

        cnt = 0
        while cnt < 5:
            bag_pos = randint(0, len(bag) - 1)
            digit = bag[bag_pos]
            pos = int(digit / 10)

            if pos == 9:
                pos = 8

            if string[pos] == '':
                bag.pop(bag_pos)
                string[pos] = digit
                cnt += 1

        return string

    def __str__(self):
        res = '{:-^27}\n'.format(self.name)
        for x in range(3):
            res += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(*self.card[x]) + '\n'
        return res + 27 * '-'


player = Rulottocard(' Игрок ')
computer = Rulottocard(' Компьютер ')

bag = [x for x in range(1, 91)]  # Мешок с бочками.

while True:
    if len(bag) < 1:
        print('Бочонков больше нет! Результаты игры:\nу компьютера осталось {} числа/чисел,\n \
        у игрока осталось {} числа/чисел.'.format(computer.count_barrel, player.count_barrel))
        break
    keg = bag.pop(randint(0, len(bag) - 1))
    print('\nНовый бочонок: {} (осталось {}) ПРОВЕРЬТЕ СВОЮ КАРТОЧКУ'.format(keg, len(bag)))
    print(computer)
    print(player)
    reply = input('Зачеркнуть цифру? (y/n/q) \nY = ДА, N = нет, Q = выход')
    reply = reply.lower()
    while len(reply) == 0 or reply not in 'ynq':
        print('\n\nНезивестный ввод\n')
        print('Новый бочонок: {} (осталось {})'.format(keg, len(bag)))
        print(computer)
        print(player)
        reply = input('Зачеркнуть цифру? (y/n/q)')
        reply = reply.lower()

    if reply == 'q':
        print('Выхожу')
        break
    elif reply == 'y':
        test = False
        for x in range(3):
            if keg in player.card[x]:
                test = True
                player.card[x][player.card[x].index(keg)] = '-'
                player.count_barrel -= 1
            if keg in computer.card[x]:
                computer.card[x][computer.card[x].index(keg)] = '-'
                computer.count_barrel -= 1
        if test:
            if player.count_barrel < 1:
                print('Вы победили!')
                break
            elif computer.count_barrel < 1:
                print('Компьютер победил!')
                break
        else:
            print('Вы проиграли! Такого числа в вашей карточке нет')
            break
    elif reply == 'n':
        test = False
        for x in range(3):
            if keg in player.card[x]:
                print('Вы проиграли! Такое число есть на вашей карточке!')
                test = True
                break
            if keg in computer.card[x]:
                computer.card[x][computer.card[x].index(keg)] = '-'
                computer.count_barrel -= 1
        if test:
            break
        if player.count_barrel < 1:
            print('Вы выиграли!')
            break
        elif computer.count_barrel < 1:
            print('Компьютер выиграл!')
            break

