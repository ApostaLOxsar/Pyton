#Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def factorial (number):
    if number < 1:
        return 1
    return number * factorial(number - 1)

number = int(input("Введите число : "))
print(f"Факториал {number} = {factorial(number)}")