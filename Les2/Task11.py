#Задача 11

number = int(input("Введите число для поиска : "))
x = 0
y = 1;
count = 2; 
while (number > y):
    y += x
    x = y - x
    print(y, end=" ")
    count += 1

if (y == number):
    print(f"\nИскомое число находится на {count} позиции")
else:
    print("-1")


