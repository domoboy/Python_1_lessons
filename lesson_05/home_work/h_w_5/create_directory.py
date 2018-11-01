# импортируем модуль os
import os
import sys

''' Сначала сделал такое решение

# создаем директорию
abs_path = os.path.abspath(__file__)  # беру абсолютный путь своего скрипта
dir_path = os.path.dirname(abs_path)  # извлекаю каталог пути
os.chdir(dir_path)  # перехожу в каталог

'''


def create_dir(my_name):

    os.chdir(os.path.dirname(sys.argv[0]))

    # создаю переменную там, где лежит скрипт, чтобы дальше создать директории
    dir_path = os.path.join(os.getcwd(), my_name)

    # создаю папки и обрабатываю ошибки
    try:
        for i in range(1, 10):
            os.mkdir(dir_path + str(i))

    except FileExistsError:
        print('Такая директория уже существует')

    except OSError:
        print('Создать директорию {} не удалось'.format(dir_path))


