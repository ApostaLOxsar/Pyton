# Задача 13

days = int(input("Введите количество дней : "))
thawDays = tempthawDays = 0

for i in range(days):
    temp = int(input(f"Введите среднесуточную температуру в {i + 1} день: "))
    if temp > 0:
        tempthawDays += 1
    elif tempthawDays > thawDays:
        thawDays = tempthawDays
        tempthawDays = 0

print(f"самая длинная оттепель длилась {thawDays} дней")