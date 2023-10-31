# В случае с английским алфавитом очки распределяются так:
word = input("введите слово: ")
summ = 0
i = 0
one = {'a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r'}
two = {'d', 'g'}
three = {'b', 'c', 'm', 'p'}
four = {'f', 'h', 'v', 'w', 'y'}
five = {'k'}
eight = {'j', 'x'}
ten = {'q', 'z'}
for el in word:
    while i < len(word):
        if word[i] in one:
            summ += 1
        elif word[i] in two:
            summ += 2
        elif word[i] in three:
            summ += 3
        elif word[i] in four:
            summ += 4
        elif word[i] in five:
            summ += 5
        elif word[i] in eight:
            summ += 8
        elif word[i] in ten:
            summ += 10
        i += 1
print(word)
print(summ)

