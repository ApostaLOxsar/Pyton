# Задача 12
import math

p = int(input("введите произведение: "))
s = int(input("введите сумму: "))

d = s * s - (4 * p)
x = (s + math.sqrt(d)) / 2

print(f"{x} + {s - x} = {s}\n{x} * {s - x} = {p}")