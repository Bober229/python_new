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

class Dino:
    def __init__(self, name, kg=1, age=1):
        self.name = name
        self.kg = kg
        self.age = age
    def printer(self):
            print(self.name, self.kg, self.age)

trex = Dino(name="T-Rex", kg = 150)
trex.printer()
