class Human():
    age = 24
    glass_color = "green"
    job = ""

class Worker(Human):
    age = 35
    parent_glass_color = "blue"
    job = "Лікар"

class Student(Human):
    parent_age = 19
    glass_color = "brown"
    university = "IT University School"

work = Worker()
stund = Student()
human = Human()
#print(human.age, human.job)
print(work.age, work.job, work.parent_glass_color)
print(stund.parent_age, stund.university, stund.glass_color)
