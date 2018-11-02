# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import sys
import os
import shutil

os.chdir(os.path.dirname(sys.argv[0]))  # меняю рабочую директорию на ту, где лежит файл

path = os.path.join(os.getcwd(), 'dir_')  # os.path.join совмещение путей

# 1.а - Создание директорий

'''

try:
    for i in range(1, 10):
        os.mkdir(path + str(i))

except FileExistsError:
    print('Такая директория уже существует')

except OSError:
    print('Создать директорию {} не удалось'.format(path))
    
'''

# 1.b - Удаление созданных директорий

'''

dir_path = os.path.join(os.getcwd(), 'dir_')  # os.path.join совмещение путей

try:
    for i in range(1, 10):
        os.rmdir(path + str(i))

except OSError:
    print('Нельзя удалить то, чего не существует')
    
'''

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

'''

print(os.listdir("."))

'''

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

'''

shutil.copy('hw05_easy.py', 'copy_hw05_easy.py', follow_symlinks=True)

'''
