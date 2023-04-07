#Задание 9

number = tempNumber= int(input("Введите n : "))
factorialNumber = 1

while (tempNumber != 1):
    factorialNumber *= tempNumber
    tempNumber -= 1

print(f"факториал {number} = {factorialNumber}")