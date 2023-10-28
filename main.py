# num = 6
# num1 = 11
# target = 333
num = 6
num1 = 11
target = 333
a = 3
b = 2
d = 0
c = 0
if num1 != a:
    c = target-num
    c = c/a-num1-num
if num1 >= num:
    d = (target/111-3) + num1
if target != num1:
    d = (d-num1)
print(f"Мінімальна кількикість монет, до суми {target}: ")
print(f"{a} монеток по {c}")
print(f"{b} по {d}")
print(b*d+a*c)