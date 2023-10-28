# num = 6
# num1 = 11
# target = 333
num = 6
num1 = 11
target = 333
a = 7
b = 5
d = target-num1
c = 0
if target != num1:
    d = target-num1
    d = d/a
if num1 >= 0:
    c = d-num

print(f"Мінімальна кількикість монет, до суми {target}: ")
print(f"{a} монеток по {c}")
print(f"{b} по {d}")