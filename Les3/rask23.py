#Задача 23
a = [0, -1, 5, 2, 3, 4]
count = 0

for x in range(1,len(a)):
   if a[x - 1] < a[x]:
        count += 1


print(count)