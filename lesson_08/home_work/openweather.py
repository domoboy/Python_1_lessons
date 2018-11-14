import os
import sys
import requests
import sqlite3

os.chdir(os.path.dirname(sys.argv[0]))  # без назначения рабочей директории мой pycharm отказывается работать
sity = input('Введите город, в котором вы желаете узнать температуру')


def get_api_key():
    """ Функция получения API KEI из файла app.id"""
    with open('app.id') as file:
        k = file.read()
    return k


def get_id_city():
    """ Функция получает ID города. В этой версии только первый результат TODO сделать выгрузку всех городов для выбора
        http://api.openweathermap.org/data/2.5/find?q=Moscow&type=like&units=metric&APPID=00a17ec7faa055c0bfeeb990c2fd2f4a
    """
    res = requests.get('http://api.openweathermap.org/data/2.5/find', params={'q': sity, 'type': 'like',
                                                                              'units': 'metric', 'APPID': get_api_key()})
    data = res.json()
    # cities = ['{} ({})'.format(d['name'], d['sys']['country']) for d in data['list']]
    # print('City: ', cities)
    city_id = data['list'][0]['id']  # забираю только первое значение ID
    return city_id


# print('City ID = ', get_id_city())


def get_weather_value():
    """ Функция получает значение погоды, ее ID и время по ID города, например Moscow, RU id= 524901
        http://api.openweathermap.org/data/2.5/weather?id=524901&units=metric&appid=00a17ec7faa055c0bfeeb990c2fd2f4a
    """
    res = requests.get('http://api.openweathermap.org/data/2.5/weather', params={'id': get_id_city(), 'units': 'metric',
                                                                                 'appid': get_api_key()})
    data_w = res.json()

    temperature = data_w['main']['temp']  # текущая температура
    id_weather = data_w['weather'][0]['id']  # id_погоды
    data_weather = data_w['dt']  # дата получения погоды

    weather = [(get_id_city(), sity, data_weather, temperature, id_weather)]

    return weather


# print('Список данных для таблицы = ', get_weather_value())


def create_database():
    """ Функция создает пустую базу данных
        Погода
            id_города           INTEGER PRIMARY KEY
            Город               VARCHAR(255)
            Дата                DATE
            Температура         INTEGER
            id_погоды           INTEGER                 # weather.id из JSON-данных
        Производится проверка, если БД нет, то создается новая, если есть, получаю данные из таблицы и сравниваю по ID
        и дате существует ли запись, если запись не совпадает с той, которую получил от сервера перезаписываю
    """
    conn = sqlite3.connect("geek_owm.db")
    cursor = conn.cursor()

    try:  # проверка на наличие таблицы
        cursor.execute('''CREATE TABLE weather (id_города INTEGER PRIMARY KEY, Город VARCHAR(255), Дата DATE,
                         Температура INTEGER, id_погоды INTEGER)''')
        conn.commit()
        cursor.executemany('INSERT INTO weather VALUES (?, ?, ?, ?, ?)', get_weather_value())
        conn.commit()

    except:  # если база есть
        try:  # проверка наличия записи о городе
            cursor.executemany('INSERT INTO weather VALUES (?, ?, ?, ?, ?)', get_weather_value())
            conn.commit()

        except:  # работаем с базой, проверяем изменилась ли дата, если да, записываем новое значение температуры
            check_value_t = 'SELECT * FROM weather WHERE id_города =?'
            cursor.execute(check_value_t, [(str(get_weather_value()[0][0]))])
            k = cursor.fetchall()
            # print('1', get_weather_value()[0][2])
            # print('2', k[0][2])
            if get_weather_value()[0][2] != k[0][2]:
                cursor.execute("""REPLACE INTO weather (id_города, Город, Дата, Температура, id_погоды) VALUES
                                 (?, ?, ?, ?, ?)""", get_weather_value())
                conn.commit()
                print('Запись обновлена')
    sql = "SELECT * FROM weather WHERE id_города=?"
    cursor.execute(sql, [(str(get_id_city()))])
    s = cursor.fetchall()
    print(s)
    print('Добавил запись в базу данных')
    conn.close()


create_database()

"""
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.

    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID,
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys

        Ключ имеет смысл сохранить в локальный файл, например, "app.id"


== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz

    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка
     (воспользоваться модулем gzip
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)

    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}


== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}


== Сохранение данных в локальную БД ==
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""
# НЕДОДЕЛАННАЯ ЗАГОТОВКА ПОЛУЧЕНИЯ ПОГОДЫ ПРИ ПОМОЩИ БИБЛИОТЕКИ PYOWM

# import pyowm  # можно было бы и так получить погоду в нужном городе
#
# owm = pyowm.OWM(key_owm[0], language='ru')
#
# observation = owm.weather_at_place(sity)  # здесь передаю данные по городу
# w = observation.get_weather()  # здесь забираю из полученных данных только данные о погоде
#
# temperature = w.get_temperature('celsius')['temp']  # здесь говорю, что мне надо только температуру в данный момент C'
#
# i_d = owm.city_id_registry()  # здесь получаю данные по ID городов
# d = i_d.ids_for(sity)  # здесь спрашиваю, какие ID вообще есть у городов
#
# cities_list = [x[2] for x in d]  # здесь у меня только значения стран
# list_id = [x[0] for x in d]  # это id из листа
#
# print(cities_list)
# print(d[1][0])
# temper_at_id = d[1][0]
# my_c = owm.weather_at_id(temper_at_id)
# dd = my_c.get_temperature('celsius'['temp'])
#
# print(dd)

# my_sity = d[1][0]  # получаю ID моего города (просто знаю что ру)
#
# print(my_sity)
# print(i_d)
# print(d)
# print('Текущая температура в {} составляет {} градусов по Цельсию'.format(sity, temperature))
# print(w)

