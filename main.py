kickk = ''
class Workers:
    def __init__(self, name, surname, old = 18, country="USA"):
        self.name = name
        self.surname = surname
        self.old = old
        self.country = country
        if kickk == self.name:
            kickk == kick

    def printer(self):
            print(self.name, self.surname, self.old, self.country)

denis = Workers(name="Денис", surname ="Міллер", old = 19, country="United Kingdom")
dmitro = Workers(name="Дмитро", surname="Геймер", old = 25, country="USA")
dgordg = Workers(name="Джордж", surname="Королевий", old = 23, country="United Kingdom")
maksym = Workers(name="Максим", surname="Дмитрович", old = 21, country="USA")

menu = input("Привіт! Це головне меню, якщо вихочите подивитись список працівників напишіть '1': \nЯкщо ви хочите змінивік людини, напишіть '2': ")
if menu == '1':
    printero = input("Виберіть людину, якої інформації хочете подивитись: ")
elif menu == '2':
    kickk = input("Впишіть старе імя: ")
    kick = input("Впишіть нове імя: ")
    if kickk == "Денис":
        denis.printer()
        break
    elif kickk == "Дмитро":
        dmitro.printer()
        break
    elif kickk == "Джордж":
        dgordg.printer()
        break
    elif kickk == "Максим":
        maksym.printer()
        break

if printero == "Денис":
    denis.printer()
elif printero == "Дмитро":
    dmitro.printer()
elif printero == "Джордж":
    dgordg.printer()
elif printero == "Максим":
    maksym.printer()