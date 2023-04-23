
s = input("Введите строку: ")
words = s.split()

char_count = {}

for word in words:
    for i, char in enumerate(word):
        if char in char_count:
            word = word[:i] + char + "_" + str(char_count[char]) + word[i+1:]
            char_count[char] += 1
        else:
            char_count[char] = 1

print(word, end=" ")

