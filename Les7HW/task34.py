
#Task34

def ritm(inputString):
    inputString = inputString.split()
    countVowel = []
    for temp in inputString:
        tempCount = 0
        for tempChar in temp:
            if tempChar in 'йуеыаоэяию':
                tempCount += 1
        countVowel.append(tempCount)
    return len(countVowel) == countVowel.count(countVowel[0])



inputStr = input("Введите строку: ")
if (ritm(inputStr)):
    print("Парам пам-пам")
else:
    print("Пам парам")
