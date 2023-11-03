class Workers:
    def __init__(self, name, surname, age = 18, country="USA"):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country

    def print(self):
        print(self.name, self.surname, self.age, self.country)

def main():
    workers = init_workers()

    while True:
        menu = input("Привіт! Це головне меню, якщо вихочите подивитись список працівників напишіть '1': \nЯкщо ви хочете змінити вік людини, напишіть '2': ")
        if menu == '1':
            for worker in workers:
                worker.print()

        elif menu == '2':
            input_name = input("Впишіть імя: ")

            worker_exist = False
            for worker in workers:
                if worker.name == input_name:
                    change_age(worker)
                    worker_exist = True
                    break

            if (not worker_exist):
                print("Працівника не існує!")

        elif menu == "exit":
            break

def init_workers():
    denis = Workers(name="Денис", surname="Міллер", age=19, country="United Kingdom")
    dmytro = Workers(name="Дмитро", surname="Геймер", age=25, country="USA")
    gorg = Workers(name="Джордж", surname="Королевий", age=23, country="United Kingdom")
    maksym = Workers(name="Максим", surname="Дмитрович", age=21, country="USA")

    return {denis, dmytro, gorg, maksym};

def change_age(worker):
    new_age = input("Напишіть, скільки працівнику років: ")
    worker.age = new_age
    worker.print()

main()