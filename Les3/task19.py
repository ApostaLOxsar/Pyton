#Задача 19

arr = [1, 2, 3, 4, 5]
k = 3

for i in range(k):
    arr.append(arr[i])
arr = arr[k:]
print(arr)