# 1 задание
print("Курс Основы программирования начался")
# 2 задание
print((16823 * 12302) % 3092)
# 3 задание
age = int(input("Введите ваш возраст -"))
name = str(input("Введите ваше имя -"))
if age >= 16:
    print("Поздравляем вы поступили в ВГУИТ")
else:
    print("Сначала нужно окончить школу!")

if 0 < age < 75:
    print("Данный возраст больше 0 и меньше 75")
else:
    print("Данный возраст не проходит")

if name == str("Иван"):
    print("Опа, а это заносик у нас!")
else:
    print("К счастью, вы не Иван")

if age <= 15:
    if age == 15:
        print("Вам ещё нужно отучиться в школе", int(16 - age), "год!")
    elif (age <= 14) and (age >= 12):
        print("Вам ещё нужно отучиться в школе", int(16 - age), "года!")
    else:
        print("Вам ещё нужно отучиться в школе", int(16 - age), "лет!")
# 4 задание 
seconds = int(input())
days = seconds // 86400 
hours = seconds // 3600 % 24
minutes = seconds // 60 % 60 
sec = seconds % 60
print(days, hours, minutes, sec, sep=':')
# 5 задание
n = int(input("Введите число -"))
d = n + n**2 + n**3 + n**4 + n**5
print(d)
# 6 задание
x = 89
y = 36
x, y = y, x
print("X =", x, "Y =", y)
# 7 задание
number = int(input("Введите число -"))
if number % 2 == 0:
    print("Это число четное!")
else:
    print("Это число не четное!")
