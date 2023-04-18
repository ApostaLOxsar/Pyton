#Задача 18


lens = int(input("введите длинну: "))
arr = []

for temp in range(lens):
    arr.append(int(input("введите элемент: ")))


foundNumb = int(input("введите искомый элемент: "))

dif1 = abs(arr[0] - foundNumb)
index = 0

for temp in range(1,len(arr)):
    dif2 = abs(arr[temp] - foundNumb)
    if (dif2 < dif1):
        dif1 = dif2
        index = temp

print(f"Ближайший к {foundNumb} это {arr[index]}")