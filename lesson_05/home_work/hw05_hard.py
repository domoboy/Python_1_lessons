# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <dir_name> - меняет текущую директорию на одну из внутренних
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


import sys
import os
import shutil

# os.chdir(os.path.dirname(sys.argv[0]))  # меняю рабочую директорию на ту, где лежит файл

print('sys.argv = ', sys.argv)
# print(os.getcwd())


def print_help():  # вывод справки

    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print('cp <file_name> - создает копию указанного файла')
    print('rm <file_name> - удаляет указанный файл')
    print('cd <dir_name> - меняет текущую директорию на одну из внутренних')
    print('ls - отображение полного пути текущей директории')


def make_dir():  # создание директории

    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return

    dir_path = os.path.join(os.getcwd(), dir_name)

    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))

    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():  # была в примере

    print("pong")


def copyfile():  # копирует файл

    if not file_name:
        print('Необходимо указать имя файла вторым параметром')
        return
    try:
        new = 'copy_' + file_name
        shutil.copy(file_name, new)
        if os.path.exists(new):
            print('Файл {} успешно создан'.format(new))
        else:
            print('Что-то пошло не так')

    except FileExistsError:
        print('Копирование не удалось! Файла {} не существует'.format(file_name))


def delfile():  # удаляет файл

    if not file_name:
        print('Необходимо указать имя файла вторым параметром')
        return

    try:
        answer = input('Вы действительно хотиет удалить {}? Ответ в формате Y / N'.format(file_name))
        if answer == 'Y':
            os.remove(file_name)
            print('Файл успешно удален')
        else:
            return

    except FileExistsError:
        print('Нельзя удалить то, чего не существует')


def replace_dir():  # меняет директорию

    if os.path.isdir(sys.argv[2]):
        os.chdir(sys.argv[2])
        print('Вы находитесь в директории: {}'.format(sys.argv[2]))

    else:
        print('Директории не существует')


def full_path():  # показывает полный путь

    print(os.getcwd())


# что делаем
do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copyfile,
    "rm": delfile,
    "cd": replace_dir,
    "ls": full_path
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")


#  Для скорости:
# python3 hw05_hard.py help
# python3 hw05_hard.py mkdir +директория
# python3 hw05_hard.py ping
# python3 hw05_hard.py cp +файл
# python3 hw05_hard.py rm +файл
# python3 hw05_hard.py cd +директория
# python3 hw05_hard.py ls
