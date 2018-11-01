# импортируем модуль os
import os
import sys


def del_directory(name):

    os.chdir(os.path.dirname(sys.argv[0]))

    # обращаюсь к папкам
    dir_path = os.path.join(os.getcwd(), name)

    # удаляю папки и обрабатываю ошибки
    try:
        for i in range(1, 10):
            os.rmdir(dir_path + str(i))

    except OSError:
        print('Нельзя удалить то, чего не существует')

