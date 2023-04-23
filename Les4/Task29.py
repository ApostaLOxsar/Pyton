#Задача 29
number = maxNumber = int(input("Введите цифру: "))


while (number != 0):
    if (number > maxNumber):
        maxNumber = number
    # значение тру if (условие) else значение елзе
    #maxNumber = number if number > maxNumber else maxNumber
    number = int(input("Введите цифру: "))

print(f"Максимальный элемент: {maxNumber}")