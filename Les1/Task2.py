import math

n = int(input("Введите количество километров за 1 день: "))
m = int(input("Введите длинну пути: "))
c = int(math.ceil(m / n))
#c = m / n
print(f"Понадобится ехать в течение {c} дней")
