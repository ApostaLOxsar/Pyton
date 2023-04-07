# Задача 6

def GetSumNumber(tempNumber):
    temp = 0
    while tempNumber > 0:
        temp += tempNumber % 10
        tempNumber //= 10
    return temp


number = int(input("Введите номер билета: "))
firstThriNumber = number // 1000
secondThriNumber = number % 1000

if GetSumNumber(firstThriNumber) == GetSumNumber(secondThriNumber):
    print("yes")
else:
    print("no")
