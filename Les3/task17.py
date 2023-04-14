
#Задача 17

a = [1, 1, 2, 0, -1, 3, 4, 4, 5, 6]
b = []
for temp in a:
    if (not temp in b):
        b.append(temp)
print (len(b))