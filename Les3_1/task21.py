#задача 21

test_list = {"V": "S001", "V": "S002", "VI": "S001", "VI": "S005", "VII": " S005 ", " V ":" S009 ", " VIII ":" S007 ", "IV":"holla", "1234": "S005"}
#res = list(set(val for dic in test_list for val in dic.values()))
a = set()

for value in test_list.values():
     a.add(value)

print(sorted(a))
