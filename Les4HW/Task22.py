#Задание 22


from pstats import SortKey


a = {1,2,3,4,2,3,4,2,3,4,2,4}
b = {5,6,3,3,2,8,4,2,9,10,2,4}
print(a)
print(b)
a = sorted(set(a))
b = sorted(set(b))
for temp in a:
    if temp in b:
        print(temp, end=" ")
