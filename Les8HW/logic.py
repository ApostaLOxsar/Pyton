
def checFile (nameFile):
    try:
        f = open(nameFile, 'r')
    except:
        f = open(nameFile, 'x')
    f.close()

def addContact(nameFile):
    f = open(nameFile, 'a')
    name = input("Введите имя: ")
    firstName =  input("Введите Фамилию: ")
    surName = input("Введите Отчество: ")
    phoneNumber = input("Введите номер телефона: ")
    f.write(name + '-' + firstName + '-' + surName + '-' + phoneNumber + '\n')
    f.close()

def printPhoneBook(nameFile):
    f = open(nameFile, 'r')
    phone = f.readlines()
    printPeople(phone)
    f.close()

def searchPeople(nameFile):
    f = open(nameFile, 'r')
    phone = f.readlines()
    people = input('Введите кого хотите найти: ')
    result = []
    for item in phone:
        if people in item:
            result.append(item)
    if len(result) != 0:
        print('Вот что нашлось: ')
        printPeople(result, 1)
    else:
        print('Таких нет')
    f.close()


def printPeople(phone, flag = 0):
    count = 1
    if flag == 0:
        for item in phone:
            print(str(count)+ ' ==>  ' + item[:-1].replace('-', '\t'))
            count += 1
    elif flag == 1:
        for item in phone:
            print(item[:-1].replace('-', '\t'))

def delPeople(nameFile):
    f = open(nameFile, 'r')
    phone = f.readlines()
    delPeople = int(input('Введите п/н кого хотите удалить: '))
    if delPeople <= len(phone) and delPeople > 0:
        print(f'Человек с данными {phone.pop(delPeople - 1)[:-1]} удален')
    else:
        print('Человека с таким индексом нет(')
    f.close()
    saveInFile(nameFile, phone)

def changePeople(nameFile):
    f = open(nameFile, 'r')
    phone = f.readlines()
    changePeople = int(input('Введите п/н кого хотите изменить: '))
    if changePeople <= len(phone) and changePeople > 0:
       name = input("Введите имя: ")
       firstName =  input("Введите Фамилию: ")
       surName = input("Введите Отчество: ")
       phoneNumber = input("Введите номер телефона: ")
       phone[changePeople - 1] = name + '-' + firstName + '-' + surName + '-' + phoneNumber + '\n'
       saveInFile(nameFile, phone)
    else:
        print('Человека с таким индексом нет(')
    f.close()

def saveInFile(nameFile, phone):
    f = open(nameFile, 'w')
    f.writelines(phone)
    f.close()