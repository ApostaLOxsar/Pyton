i = int(input("Введите номер вагона в который Витя сел: "))
j = int(input("Введите номер вагона который видит Витя: "))

if (i != j):
    print(f"Количество вагонов в поезде равно {i + j - 1}")
else:
    print("Недостаточно информации")