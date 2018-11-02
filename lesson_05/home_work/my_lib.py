import os


# функция создания папки
def create_folder(name):  # Создает папку
    dir_path = os.path.join(os.getcwd(), name)  # os.path.join совмещение путей
    try:
        os.mkdir(dir_path)
        print('Папка успешно создана!')

    except FileExistsError:
        print('Такая директория уже существует')


# функция для удаления папки
def del_folder(name):  # удаляет папку

    dir_path = os.path.join(os.getcwd(), name)  # os.path.join совмещение путей

    try:
        os.rmdir(dir_path)
        print('Папка успешно удалена!')

    except OSError:
        print('Нельзя удалить то, чего не существует')


# функция перемещения в нужную директорию
def goto_folder():

    path = input('В какой директории вы хотите работать? Укажите адрес')

    if os.path.isdir(path):

        os.chdir(path)
        print('Вы перешли в директорию {}'.format(path))

    else:
        print('Что-то пошло не так. Такой директории не существует')


# функция, которая показывает содержимое папки
def show_contents():

    print(os.listdir("."))

