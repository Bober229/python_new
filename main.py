words = ["Поле", "Урок", "Дота", "Чудо"]
import random
#randnum = random.randint(0, 3)
randnum = random.randint(0, 1)
print(words[randnum])
print(len(words))
startgame = input("Вітаємо, друже у грі. Поле Чудес! Якщо ти готовий, нажми 'ENTER' (P:S У вас 5 спроб!) ")
if words == words:
    for playerword in range(5):
        if words[randnum] == "Поле":
            print("Місце де садять овочі?")
            word = input("Впишіть букву:")
            if len(word) == words[randnum]:
                if word == words:
                    print("Ура! Ви вгадали усе слово! Вітаємо!")
                    print(words)
                    break
                else:
                    print("О ніі!! Ви хотіли вгадати усе слово? Але у вас не вийшло! Гра закінчилась!")


            elif word == words[0] or words[1] or words[2] or words[3]:
                print("Чудово! Ви вгадали перше слово!")
                if len(words) >= 4 and word == words[0]:
                    print(f"{words[0]}■■■")
            else:
                print("Викличте адмінів, гра зламалась :o ")
        if words[randnum] == "Урок":
            print("Де сидять школярі?")
            word = input("Впишіть букву:")
            if len(word) == words[randnum]:
                if word == words[randnum]:
                    print("Ура! Ви вгадали усе слово! Вітаємо!")
                    print(words)
                    break
                else:
                    print("О ніі!! Ви хотіли вгадати усе слово? Але у вас не вийшло! Гра закінчилась!")


            elif word == words[0] or words[1] or words[2] or words[3]:
                print("Чудово! Ви вгадали перше слово!")
                if len(words) >= 4 and word == words[0]:
                    print(f"{words[0]}■■■")
            else:
                print("Викличте адмінів, гра зламалась :o ")