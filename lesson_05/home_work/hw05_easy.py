# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import sys
import os
import delete_directory as dld

os.chdir(os.path.dirname(sys.argv[0]))

# delete_directory.del_directory('dir_')


print('os.getcwd = ', os.getcwd())
print('sys.argv = ', sys.argv)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

