# Задача 2

number = numberTemp = int(input("Введите число "))
summ = 0


while numberTemp > 0:
    summ += numberTemp % 10
    numberTemp //= 10

print(f"Сумма цифр в числе {number} = {summ}")