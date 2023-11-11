# # class Human():
# #     age = 24
# #     glass_color = "green"
# #     job = ""
# #
# # class Worker(Human):
# #     age = 35
# #     parent_glass_color = "blue"
# #     job = "Лікар"
# #
# # class Student(Human):
# #     parent_age = 19
# #     glass_color = "brown"
# #     university = "IT University School"
# #
# # work = Worker()
# # stund = Student()
# # human = Human()
# # #print(human.age, human.job)
# # print(work.age, work.job, work.parent_glass_color)
# # print(stund.parent_age, stund.university, stund.glass_color)
#
# class University():
#     name = "Epic IT"
#
# class Group(University):
#     mushstudent = "13"
#     group = "4"
#
# class Students(Group):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def printer(self):
#         print(self.name, self.age)
#
#
# pavel = Students(name="Павло", age="16")
# vadim = Students(name="Вадим", age="17")
# oleksander = Students(name="Олександр", age="15")
# class Teachers(University):
#     def __init__(self, tname, tage):
#         self.tname = tname
#         self.tage = tage
#
#     def printer(self):
#         print(self.tname, self.tage)
# dmitro = Teachers(tname="Дмитро", tage="24")
# pavel = Teachers(tname="Павло", tage="18")
# denis = Teachers(tname="Денис", tage="31")
# a = int(input("Введіть 1 - додати вчителя/вивести вчителів. \nВведіть 2 - додати студента/вивести студентів: "))
# if a == 1:
#     teacher = int(input("Що ви хочите? Вивести вчителів - 1, додати вчителів - 2: "))
#     if teacher == 1:
#         dmitro.printer()
#         pavel.printer()
#         denis.printer()
#     if teacher == 2:
#         newname = input("Введіть імя, нового вчителя: ")
#         newage = input("Введіть вік, нового вчителя: ")
#         newname = Teachers(tname=f"{newname}", tage=f"{newage}")
#         dmitro.printer()
#         pavel.printer()
#         denis.printer()
#         newname.printer()
# if a == 2:
#     students = int(input("Що ви хочите? Вивести вчителів - 1, додати вчителів - 2: "))
#     if students == 1:
#         dmitro.printer()
#         pavel.printer()
#         denis.printer()
#     if students == 2:
#         newname = input("Введіть імя, нового вчителя: ")
#         newage = input("Введіть вік, нового вчителя: ")
#         newname = Teachers(tname=f"{newname}", tage=f"{newage}")
#         dmitro.printer()
#         pavel.printer()
#         denis.printer()
#         newname.newteacher()
#
# class Subjects(Students, Teachers):
#     subs = ["Математика", "ІТ", "Фізика", "Фізкультура"]
#     marks = [12,11,9,11]
#
# # univer = University()
# # group = University()
# # stund = Students()
# # subjects = Subjects()
# # #print(human.age, human.job)
# # print(group.name)
# # print(subjects.subs)
# # print(subjects.marks)

# class Grandparent():
#     def hello(self):
#         print("hello") #public
#     def _hello(self):
#         print("_hello") #protected
#     def __hello(self):
#         print("__hello") #privat
#
# a = Grandparent()
#
# a.hello()
# a._hello()
# a._Grandparent__hello()

# class Parent():
#     hello = "Hello"
#     _hello = "_Hello"
#     __hello = "__Hello"
#     def __init__(self):
#         self.world = "World"
#         self._world = "_World"
#         self.__world = "__World"
#
#     def pr(self):
#         print(self.hello)
#         print(self.world)
#         print(self._hello)
#         print(self._world)
#         print(self.__hello)
#         print(self.__world)
# class Hi(Parent):
#     def hi_pr(self):
#         print(self.hello)
#         print(self.world)
#         print(self._hello)
#         print(self._world)
#         print(self._Parent__hello)
#         print(self._Parent__world)
# a = Parent()
# b = Hi()
# a.pr()
# b.hi_pr()
p = input("Введіть свій пароль: ")
pas = [p]
len == len(pas)
menu = input("Вітаємо у щодденику. Подивитись росклад - 1, подивитись пароль - 2.")
class Student():
    def __init__(self, name):
        self.name = name
    def printer(self):
        print(self.name)
student = Student(name="Вадим")

class Diary(Student):
    password = pas
    def __init__(self, password):
        self.password = pas
        self.__password = pas
    def defaultp(self):
        print(self.password)
    def secretp(self, __password):
        print(self.__password)

diary = Diary(password=pas)
# for checkpass in len:
#     check = 1 * len(p)
#     if check == len(p):
#         print(f"{check}")

class Subject(Student):
    def __init__(self, subject):
        self.subject = subject
    def printer(self):
        print(self.subject)
subject = Subject(subject=["Фізкультура","Математика","ІТ","Фізика","Біологія","Хімія"])
if menu == "1":
    student.printer()
    subject.printer()
if menu == "2":
    passwordcheck = int(input("Яким чином, ви хочите вивести пароль? 1 - простий, 2 - засекречиний."))
    if passwordcheck == 1:
        diary.defaultp()
    if passwordcheck == 2:
        diary.secretp()
# 3 класи 2 дочірних. 1 батьківський. Студент, щоденник, предмет. Треба додати можливість виводити його розклад та пароль.Якщо він виводить пароль через print(password) - виводиться пароль зірочками. Якщо приватом - виводиться сам пароль.