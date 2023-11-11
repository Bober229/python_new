# class Human():
#     age = 24
#     glass_color = "green"
#     job = ""
#
# class Worker(Human):
#     age = 35
#     parent_glass_color = "blue"
#     job = "Лікар"
#
# class Student(Human):
#     parent_age = 19
#     glass_color = "brown"
#     university = "IT University School"
#
# work = Worker()
# stund = Student()
# human = Human()
# #print(human.age, human.job)
# print(work.age, work.job, work.parent_glass_color)
# print(stund.parent_age, stund.university, stund.glass_color)

class University():
    name = "Epic IT"

class Group(University):
    age = 35
    parent_glass_color = "blue"
    job = "Лікар"

class Students(Group):
    age = 19
    name = "Денис"
    parent_group = "4"

class Teacher(University):
    tname = "Дмитро"
    tage = 24
    parent_group = ""
    

class Subjects(Students, Teacher):
    subname = "Інформатика"
    mark = "10"

#a = int(input("Введіть 1 - додати вчителя. \nВведіть 2 - щоб додат студента:"))

univer = University()
group = University()
stund = Students()
teacher = Teacher()
subjects = Subjects()
#print(human.age, human.job)
print(group.p)
print(stund.parent_age, stund.university, stund.glass_color)
