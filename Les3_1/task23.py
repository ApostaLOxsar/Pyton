#Задача 23

arr = [0, -1, 5, 2, 3, 4, 0]
count = 0

for x in range(1, len(arr)):
    if arr[x - 1] < arr[x]:
        count += 1

print(count)