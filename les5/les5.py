



def reversArr(n, i):
    if i == 0:
        return 1
    else:
        print(n[i])
        return reversArr(n, i-1)

n = (1,2,3,4,5,6,7,8)
print(reversArr(n, len(n)-1))


grades = input().split() 
#grades = list(map(int, grades))
min_grade = min(grades) 
max_grade = max(grades)


for i in range(len(grades)):
    if grades[i] == max_grade:
        grades[i] = min_grade

print(' '.join(map(str, grades)))