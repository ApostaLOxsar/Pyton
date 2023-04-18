
# Задача 16
lens = int(input("введите длинну: "))
arr = ""

for temp in range(lens):
    arr += input("введите элемент: ")


foundNumb = input("введите искомый элемент: ")
count = 0
for temp in arr:
    count = count + 1 if (temp == foundNumb) else count

print(f"Мы имеем {count} элементов {foundNumb}")