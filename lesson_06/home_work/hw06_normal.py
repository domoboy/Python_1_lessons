# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

'''

Видимо как-то так. Классы и методы которые в этих классах должны происходить

школа:
- получить список классов
- получить список учителей преподающих в определенном классе
- получить список учеников класса

люди:
    учителя(ФИО, предмет):
         - получить список классов в которых он преподает
    ученик(ФИО,мама,папа):
         - получить список родителей ученика

'''


class School:

    def __init__(self):
        # self.classroom = classroom  # класс
        # self.school_object = school_subject  # школьный предмет
        self.students = []
        self.teachers = []

    def add_teacher(self, new_teacher):
        self.teachers.append(new_teacher)

    def print_teachers(self):
        for teacher in self.teachers:
            print(teacher.what_teaches())

    def add_student(self, new_student):
        self.students.append(new_student)

    def print_students(self):
        for student in self.students:
            print(student.get_parents())



class Person:

    def __init__(self, name, patronymic, surname):
        self.name = name  # имя
        self.patronymic = patronymic  # отчество
        self.surname = surname  # фамилия

    def full_name(self):  # получаю строку с полным ФИО в формате Фамилия И. О.
        return self.surname + ' ' + self.name[:1] + '. ' + self.patronymic[:1] + '.'

    def fullname_big(self):  # возвращает ФИО  в полном формате Фамилия Имя Отчество
        return self.surname + ' ' + self.name + ' ' + self.patronymic


class Student(Person):

    def __init__(self, name, patronymic, surname, mom, dad):
        Person.__init__(self, name, patronymic, surname)
        self.mom = mom
        self.dad = dad

    def get_parents(self):  # получить список родителей ученика
        return 'Ученик {}:\nЕго родители, мама {} и папа {}'.format(Student.full_name(student), self.mom, self.dad)


class Teacher(Person):

    def __init__(self, surname, name, patronymic, class_object):
        Person.__init__(self, name, patronymic, surname)
        self.class_object = class_object

    def what_teaches(self):
        return '{} это предмет, который преподает {}'.format(self.class_object.title(), Teacher.fullname_big(teacher))


students = [Student('Иван', 'Иванович', 'Иванов', 'Иванова Ангелина Тарасовна', 'Иванов Иван Петрович'),
            Student('Петр', 'Петрович', 'Петров', 'Петрова Галина Сергеевна', 'Петров Петр Семенович'),
            Student('Сидор', 'Сидорович', 'Сидоров', 'Сидорова Тамара Ивановна', 'Сидоров Сидор Альбертович'),
            Student('Николай', 'Николаевич', 'Николаев', 'Николаева Алла Ивановна', 'Николаев Николай Иванович'),
            Student('Геннадий', 'Петрович', 'Лукин', 'Лукина Ольга Борисовна', 'Лукин Петр Иванович'),
            Student('Мария', 'Леонидовна', 'Сухова', 'Сухова Елизавета Игоревна', 'Сухов Леонид Гаврилович'),
            Student('Елизавета', 'Сергеевна', 'Карпенюк', 'Карпенюк Марина Сергеевна', 'Карпенюк Сергей Иванович'),
            Student('Александр', 'Кимович', 'Ли', 'Ли Мария Борисовна', 'Ли Ким Чинович'),
            Student('Алла', 'Семеновна', 'Багрянцева', 'Багрянцева Тамара Валерьевна', 'Багрянцев Семен Иванович'),
            Student('Ефим', 'Иванович', 'Тимофеев', 'Тимофеева Анна Семеновна', 'Тимофеев Иван Тарасович'),
            Student('Игорь', 'Борисович', 'Трапов', 'Трапова Инга Игоревна', 'Трапов Борис Алексеевич'),
            Student('Галина', 'Ивановна', 'Жилкина', 'Жилкина Элла Ивановна', 'Жилкин Иван Николаевич'),
            Student('Сергей', 'Петрович', 'Тюльпанов', 'Тюльпанова Любовь Ивановна', 'Тюльпано Петр Сергеевич'),
            Student('Тарас', 'Иванович', 'Прохоров', 'Прохорова Ольга Николаевна', 'Прохоров Иван Иванович'),
            Student('Анна', 'Петровна', 'Гунько', 'Богоусько Анна Ивановна', 'Гунько Петр Олегович'),
            Student('Кристина', 'Леонидовна', 'Беспалова', 'Беспалова Ольга Семеновна', 'Беспалов Леонид Германович'),
            Student('Иван', 'Николаевич', 'Суворов', 'Суворова Алена Игоревна', 'Суворов Николай Семенович'),
            Student('Софья', 'Александровна', 'Петина', 'Петина Олеся Борисовна', 'Петин Алексндр Иванович'),
            ]
teachers = [Teacher('Матвеев', 'Иван', 'Герасимович', 'математика'),
            Teacher('Иванов', 'Петр', 'Васильевич', 'информатика'),
            Teacher('Руденко', 'Мария', 'Изольдовна', 'русский язык'),
            Teacher('Алексанян', 'Карен', 'Ашотович', 'математика'),
            Teacher('Головенко', 'Инна', 'Валерьевна', 'ИЗО'),
            Teacher('Степанов', 'Эдуард', 'Валентинович', 'химия'),
            Teacher('Тарасова', 'Анна', 'Ивановна', 'русский язык'),
            ]


school = School()

for teacher in teachers:
    school.add_teacher(teacher)

for student in students:
    school.add_student(student)

school.print_teachers()
# school.print_students()

'''
1. Имя
2. Фамилия
3. Отчество
4. Персона
4.2. учитель (Матвеев Иван Герасимович, Иванов Петр Васильевич, Руденко Мария Изольдовна, Алексанян Карен Ашотович,
              Головенко Инна Валерьевна, Степанов Эдуард Валентинович, Тарасова Анна Ивановна)
8. Класс (5 А, 6 Б, 8 Г)
9. Предмет (математика, русский язык, химия, информатика, ИЗО, химия)



1. Имя
2. Фамилия
3. Отчество
4. Персона
4.1. ученик ( Иванов Иван Иванович, Петров Петр Петрович, Сидоров Сидор Сидорович, Николаев Николай Николаевич,
              Лукин Геннадий Петрович, Сухова Мария Леонидовна, Карпенюк Елизавета Сергеевна, Ли Александр Кимович,
              Багрянцева Алла Семеновна, Тимофеев Ефим Иванович, Трапов Игорь Борисович, Жилкина Галина Ивановна,
              Тюльпанов Сергей Петрович, Прохоров Тарас Иванович, Гунько Анна Петровна, Беспалова Кристина Леонидовна,
              Суворов Иван Николаевич, Петина Софья Александровна )
4.1.1. папа ( Иванов Иван Петрович, Петров Петр Семенович, Сидоров Сидор Альбертович, Николаев Николай Иванович,
              Лукин Петр Иванович, Сухов Леонид Гаврилович, Карпенюк Сергей Иванович, Ли Ким Чинович,
              Багрянцев Семен Иванович, Тимофеев Иван Тарасович, Трапов Борис Алексеевич, Жилкин Иван Николаевич,
              Тюльпано Петр Сергеевич, Прохоров Иван Иванович, Гунько Петр Олегович, Беспалов Леонид Германович,
              Суворов Николай Семенович, Петин Алексндр Иванович )
4.1.2. мама ( Иванова Ангелина Тарасовна, Петрова Галина Сергеевна, Сидорова Тамара Ивановна, Николаева Алла Ивановна,
              Лукина Ольга Борисовна, Сухова Елизавета Игоревна, Карпенюк Марина Сергеевна, Ли Мария Борисовна,
              Багрянцева Тамара Валерьевна, Тимофеева Анна Семеновна, Трапова Инга Игоревна, Жилкина Элла Ивановна,
              Тюльпанова Любовь Ивановна, Прохорова Ольга Николаевна, Богоусько Анна Ивановна, Беспалова Ольга Семеновна,
              Суворова Алена Игоревна, Петина Олеся Борисовна )
4.2. учитель (Матвеев Иван Герасимович, Иванов Петр Васильевич, Руденко Мария Изольдовна, Алексанян Карен Ашотович,
              Головенко Инна Валерьевна, Степанов Эдуард Валентинович, Тарасова Анна Ивановна)
8. Класс (5 А, 6 Б, 8 Г)
9. Предмет (математика, русский язык, химия, информатика, ИЗО, химия)


students = [Student('Иванов', 'Иван', 'Иванович', '__mom__', '__dad__', '5 А', 'school_subject', 'teacher_list'),
            Student('Петров', 'Петр', 'Петрович', '__mom__', '__dad__', '5 А', 'school_subject', 'teacher_list'),
            Student('Сидоров', 'Сидор', 'Сидорович', '__mom__', '__dad__', '5 А', 'school_subject', 'teacher_list'),
            Student('Николаев', 'Николай', 'Николаевич', '__mom__', '__dad__', '5 А', 'school_subject', 'teacher_list'),
            Student('Лукин', 'Геннадий', 'Петрович', '__mom__', '__dad__', '5 А', 'school_subject', 'teacher_list'),
            Student('Сухова', 'Мария', 'Леонидовна', '__mom__', '__dad__', '5 А', 'school_subject', 'teacher_list'),
            Student('Карпенюк', 'Елизавета', 'Сергеевна', '__mom__', '__dad__', '6 Б', 'school_subject', 'teacher_list'),
            Student('Ли', 'Александр', 'Кимович', '__mom__', '__dad__', '6 Б', 'school_subject', 'teacher_list'),
            Student('Багрянцева', 'Алла', 'Семеновна', '__mom__', '__dad__', '6 Б', 'school_subject', 'teacher_list'),
            Student('Тимофеев', 'Ефим', 'Иванович', '__mom__', '__dad__', '6 Б', 'school_subject', 'teacher_list'),
            Student('Трапов', 'Игорь', 'Борисович', '__mom__', '__dad__', '6 Б', 'school_subject', 'teacher_list'),
            Student('Жилкина', 'Галина', 'Ивановна', '__mom__', '__dad__', '8 Г', 'school_subject', 'teacher_list'),
            Student('Тюльпанов', 'Сергей', 'Петрович', '__mom__', '__dad__', '8 Г', 'school_subject', 'teacher_list'),
            Student('Прохоров', 'Тарас', 'Иванович', '__mom__', '__dad__', '8 Г', 'school_subject', 'teacher_list'),
            Student('Гунько', 'Анна', 'Петровна', '__mom__', '__dad__', '8 Г', 'school_subject', 'teacher_list'),
            Student('Беспалова', 'Кристина', 'Леонидовна', '__mom__', '__dad__', '8 Г', 'school_subject', 'teacher_list'),
            Student('Суворов', 'Иван', 'Николаевич', '__mom__', '__dad__', '8 Г', 'school_subject', 'teacher_list'),
            Student('Петина', 'Софья', 'Александровна', '__mom__', '__dad__', '8 Г', 'school_subject', 'teacher_list')
            ]

teachers = [Teacher('Матвеев', 'Иван', 'Герасимович', '5 А, 8 Г', 'математика'),
            Teacher('Иванов', 'Петр', 'Васильевич', '6 Б, 8 Г', 'информатика'),
            Teacher('Руденко', 'Мария', 'Изольдовна', '5 А', 'русский язык'),
            Teacher('Алексанян', 'Карен', 'Ашотович', '6 Б', 'математика'),
            Teacher('Головенко', 'Инна', 'Валерьевна', '5 А', 'ИЗО'),
            Teacher('Степанов', 'Эдуард', 'Валентинович', '8 Г', 'химия'),
            Teacher('Тарасова', 'Анна', 'Ивановна', '6 Б, 8 Г', 'русский язык'),
            ]

'''




