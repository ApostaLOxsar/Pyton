#Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
#a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#Требуется найти N-е число Фибоначчи

def fibon(number):
    if number < 1:
        return 0
    if number in (1,2):
        return 1 
    return fibon(number - 1) + fibon(number - 2)


number = int(input("Введите искомое число : "))
print(f"Чило фибоначи {number} = {fibon(number)}")