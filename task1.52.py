x = int(input("Введите сколько килограмм конфет: "))
y = int(input("Введите сколько килограмм печенья: "))
z = int(input("Введите сколько килограмм яблок: "))
s1 = int(input("Стоимость конфет в рублях: "))
s2 = int(input("Стоимость печенья в рублях: "))
s3 = int(input("Стоимость яблок в рублях: "))
all = (x * s1) + (y * s2) + (z * s3)
print("Всего вы купили", all, "р")