vowels = ['a', 'e', 'i', 'o', 'u']
word = input("please input a word: ")
dict_1 = {}
for i in vowels:
    dict_1[i] = 0

for i in word:
    if i in vowels:
        dict_1[i] += 1

for x, y in dict_1.items():
    print(str(x) + "出现了" + str(y) + "次")
