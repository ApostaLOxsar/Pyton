# Задача 8

n = int(input("Введите  размер n: "))
m = int(input("Введите  размер m: "))
k = int(input("Введите  размер k: "))

if n * m < k:
    print("\nВы хоите слишком много")
elif n * m == k:
    print("\nВы забрали ввесь шоколад")
elif k % n == 0 or k % m == 0:
    print("\nyes")
else:
    print("\nno")