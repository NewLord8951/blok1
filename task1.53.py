mo = int(input("Стоимость монитора в рублях: "))
sb = int(input("Стоимость системного блока в рублях: "))
k = int(input("Стоимость клавиатуры в рублях: "))
m = int(input("Стоимость мыши в рублях: "))
kol = int(input("Введите колличество компьютеров: "))
sum = (mo + sb + k + m) * kol
print("Всё стоит", sum, "р")
