# a = int(input("Введіть число: "))
# sum = 0
# i = 0
# while sum <= 100:
#     print(sum)
#     sum += a
#     # print(f"Число зміної a дорівнює {a}")
#     i += 1
# print(i)

# a = ["ananas","apple","peach","candy","pear","neracuja","lemon","sweets"]
# for i in range(1):
#     if i == "candy" or i == "sweets":
#             a.remove(i)
#     # a.remove("candy")
#     # a.remove("sweets")
# print(a)
# a = 5
# def add():
#     a = 3
#     a += 5
#     print(a)
#
# add()
# print(a)

# class Student:
#     def __init__(self, name, age=12):
#         self.name = name
#         self.age = age
#     def printer(self):
#         print(self.name, self.age)
#
#
# danylo = Student(name="Danylo", age = 13)
# zlata = Student(name="Zlata", age = 15)
# zlata.printer()

# class Animals:
#     def __init__(self, name, kg=1, age=1):
#         self.name = name
#         self.kg = kg
#         self.age = age
#     def printer(self):
#             print(self.name, self.kg, self.age)
#     def grow(self,age=1):
#             self.age += age
#
# dog = Animals(name="Dog", kg = 5, age=3)
# cat = Animals(name="Cat", kg = 8, age=4)
#
# dog.grow(2)
# dog.printer()
# cat.printer()
class Films:
    def __init__(self, name, time = 60, views = 0, country="USA"):
        self.name = name
        self.time = time
        self.views = views
        self.country = country
    def printer(self):
            print(self.name, self.time, self.views, self.country)

# if Films >= 1:
#     print("Films", Films)

spiderman = Films(name="Spider-Man 2", time = 60, views = 10000, country="USA")
batman = Films(name="BatMan 2022", time = 65, views = 15000, country="USA")
opengamer = Films(name="OpenGamer", time = 120 , views = 1000000, country="United Kingdom")
deadpul = Films(name="Deadpool 2", time = 180, views = 100000, country="USA")
spiderman.printer()
batman.printer()
opengamer.printer()
deadpul.printer()

# зірочка рахування кількість фільмів скільки створили
