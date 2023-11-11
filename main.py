class Human():
    age = 24
    job = "-"

class Worker(Human):
    age = 35
    job = "Офісник працівник"

class Student(Human):
    age = 19
    parent_job = "-"

work = Worker()
stund = Student()
human = Human()
#print(human.age, human.job)
print(work.age, work.job)
print(stund.age, stund.job)
