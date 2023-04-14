# Задача 21

arr = {"V": "S001", "V ": "S002", "VI": "S001","VI ": "S005", "VII": "S005", " V ":"S009", " VIII":"S007"}
countTemp = 0;
arrTemp = arr.copy();


for key in arr:
	countTemp = 0;
	for values1 in arrTemp.values():
		if arr[key] == values1:
			countTemp += 1 
	if countTemp > 1:
		arrTemp.pop(key)

arr = arrTemp.copy()

for printTemp in arr.values(): 
	print(printTemp)

