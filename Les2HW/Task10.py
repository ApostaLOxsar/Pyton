# Задача 10


coin = int(input("Введиет кол-во монет\t:"))
coinzero = coinone = 0
for coin in range(coin):
    temp = int(input("0 or 1\t: "))
    if temp == 0:
        coinzero += 1
    elif temp == 1:
        coinone +=1

print(coinone if (coinzero >= coinone) else coinzero)