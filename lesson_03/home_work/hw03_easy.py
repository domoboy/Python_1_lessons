# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

a = input("Введите любое десятичное число")  # TODO проверить что введена точка
b = int(input("До какого кол-ва знаков сократить? Где округление до десятых, это 1, до сотых = 2, до тысячных = 3 "))


def round_off():
    c = a.split(".")  # разделили введенное значение
    d = c[1]  # дробная часть
    my_in = int(c[0])  # привели целую часть к числу
    e = int(d[:b])  # срез N символов дробной части от начала, до длины указанной пользователем

    if int(d[b]) >= 5:  # если число по индексу b больше или равно 5
        e += 1  # прибавляем единицу к числу среза, тем самым увеличивая значение на 1

    print(str(my_in) + "." + str(e))


round_off()

# while len(str(e)) < b:
# TODO добавить добавление нулей
#     e = "0" * (b - len((str(e)) + e)

# if len(str(e)) < b:
# TODO после запятой меньше символов, чем указал пользователь для сокращения
#     f += 1
#     e = 0

'''
Нужно сделать несколько дополнительных проверок:
- что если нужно будет увеличивать 9 
- что если пользователь ввел не точку, а запятую
- что если пользователь указал кол-во знаков больше, чем есть в дробной части
'''


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

#  Вариант 1
def lucky(ticket):
    n = list(str(ticket)) # делаю список
    y = int(n[0]) + int(n[1]) + int(n[2])  # присваиваю a сумму срезов от 0 до 2
    z = int(n[3]) + int(n[4]) + int(n[5])  # присваиваю a сумму срезов от 3 до 5
    return y == z  # возвращаю результат сравнения


lucky("123321")
print("Это счастливый билет")
lucky("543346")
print("Повезет в другой раз")


# Вариант 2
def is_lucky(tick):
    t = tuple(map(int, tick))  # делаю кортеж с использованием map
    n = len(tick) // 2  # получаю целую часть от деления длины ticket
    return sum(t[:n]) == sum(t[n:])  # возвращаю сравнение срезов до n и после нее


is_lucky('123231')
print("Это счастливый билет")
is_lucky('123232')
print("Повезет в другой раз")





