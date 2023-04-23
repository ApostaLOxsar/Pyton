# Задание 24

n = int(input("количество "))
arr = list()
for i in range(n):
    temp = int(input("куст "))
    arr.append(temp)

arr_count = list()
for i in range(len(arr)):
    arr_count.append(arr[i-2] + arr[i-1]+ arr[i])

print(max(arr_count))