import numpy as np
list_1 = [0, 2, 3, 6]
list_2 = np.array([0, 3, 6])
list_3 = np.arange(8)
list_4 = np.zeros((8, 9))
phrase = "Don't panic,OK?"
list_5 = list(phrase)

print(list_5[9:6:-1])
print(list_5[3:8:3])
list_6 = list_5.copy()
print(list_5.pop(6))
list_5.remove("o")
print(list_5)
print(list_6)

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("please input a word: ")

for letter in word:
    if letter in vowels:
        print(letter)