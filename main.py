# a = int(input("Введіть число: "))
# sum = 0
# i = 0
# while sum <= 100:
#     print(sum)
#     sum += a
#     # print(f"Число зміної a дорівнює {a}")
#     i += 1
# print(i)

a = ["ananas","apple","peach","candy","pear","neracuja","lemon","sweets"]
for i in range(1):
    if i == "candy" or i == "sweets":
            a.remove(i)
    # a.remove("candy")
    # a.remove("sweets")
print(a)