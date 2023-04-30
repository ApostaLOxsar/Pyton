#Задача 30:  Заполните массив элементами арифметической прогрессии. 
#Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.


firstNumber = int(input("Введите первый элемент: "))
diferent = int(input("Введите разность: "))
countNumber = int(input("Введите количество элементов: "))

arr = list()
arr.append(firstNumber)
for i in range(1,countNumber):
    arr.append(arr[i -1] * diferent)

print(arr)