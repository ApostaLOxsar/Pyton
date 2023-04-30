# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def summ (numberA, numberB):
    if numberB < 1:
        return numberA
    return summ(numberA + 1, numberB - 1)

numberA = int(input("Введите число A: "))
numberB = int(input("Введите число B: "))

print(f"Сумма {numberA} + {numberB} = {summ(numberA, numberB)}")