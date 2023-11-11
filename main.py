words = ["Поле", "Поле", "Дота", "Чудо"]
import random
#randnum = random.randint(0, 3)
randnum = random.randint(0, 1)
print(words[randnum])
print(len(words))
lens = len(words)
sword = ""
if words[randnum] == "Поле":
    sword = "Поле"
print(sword[1])
startgame = input("Вітаємо, друже у грі. Поле Чудес! Якщо ти готовий, нажми 'ENTER' (P:S У вас 5 спроб!) ")
if words == words:
    for playerword in range(1):
        if words[randnum] == "Поле":
            word = input("Впишіть першу букву:")
            if word == sword[0] or sword[1] or sword[2] or sword[3]:
                if word == sword[0]:
                    print(f"{word}■■■")
                elif word == sword[1]:
                    print(f"■{word}■■")
                elif word == sword[2]:
                    print(f"■■{word}■")
                elif word == sword[3]:
                    print(f"■■{word}")
                print("Чудово! Ви вгадали першу букву!")
            wordt = input("Впишіть другу букву:")
            if wordt == sword[0] or sword[1] or sword[2] or sword[3] or sword[4]:
                print("Чудово! Ви вгадали другу букву!")
                if wordt == sword[1] and word == sword[0]:
                    print(f"{word}{wordt}■■")
                elif wordt == sword[3] and word == sword[1]:
                    print(f"{wordt}{word}■■")
                elif wordt == sword[3] and word == sword[2]:
                    print(f"■■{word}{wordt}")
                elif wordt == sword[3] and word == sword[2]:
                    print(f"■{wordt}{word}")
                elif wordt == sword[1] and word == sword[2]:
                    print(f"■{word}{wordt}")
            wordth = input("Впишіть третью букву:")
            if word == sword[0] or sword[1] or sword[2] or sword[3]:
                print("Чудово! Ви вгадали третью букву!")
                if wordth == sword[0] and word == sword[1] and wordt == sword[2]:
                    print(f"{wordth}{word}■■")
                elif wordth == sword[1] and word == sword[0] and wordt == sword[3]:
                    print(f"{word}{wordth}■{wordth}")
                elif wordth == sword[2] and word == sword[3] and wordt == sword[0]:
                    print(f"{wordth}■{wordth}{word}")
                # elif wordt == sword[3] and word == sword[2]:
                #     print(f"■■{word}")
            wordf = input("Впишіть четверту букву:")
            if wordf == sword[0] or sword[1] or sword[2] or sword[3]:
                print("Чудово! Ви вгадали четверту букву!")
                if wordt == sword[1] and word == sword[0]:
                    print(f"{word}{wordt}■■")
                elif wordt == sword[3] and word == sword[1]:
                    print(f"■{word}■■")
                elif wordt == sword[3] and word == sword[2]:
                    print(f"■■{word}■")
                elif wordt == sword[4] and word == sword[3]:
                    print(f"■■{word}")
            else:
                print("Викличте адмінів, гра зламалась :o ")
        # if words[randnum] == "Урок":
        #     print("Де сидять школярі?")
        #     word = input("Впишіть букву:")
        #     if word == words[0] or words[1] or words[2] or words[3]:
        #         print("Чудово! Ви вгадали перше слово!")
        #         if lens == 4 and word == words[0]:
        #             print(f"{words[0]}■■■")
        #     else:
        #         print("Викличте адмінів, гра зламалась :o ")