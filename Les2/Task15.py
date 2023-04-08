#Задача 15

quantWatermelon = int(input("Введите количество арбузов : "))
minWater = maxWater = int(input(f"Введите ввес арбуза : "))


for i in range(1, quantWatermelon):
    temp = int(input(f"Введите ввес арбуза : "))
    if(temp > maxWater):
        maxWater = temp
    elif (temp < minWater):
        minWater = temp

print(f"Для тещи {minWater}")
print(f"Для себя {maxWater}")