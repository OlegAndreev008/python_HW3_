# Требуется найти в массиве list_1 самый близкий по величине
# элемент к заданному числу k и вывести его.
list_1 = []
count = int(input("сколько эл-тов будет в массиве: "))
for i in range(count):
    el = int(input(f"значение {i + 1} эл-та: "))
    list_1.append(el)
k = int(input("введите значение эл-та: "))
diff = k - list_1[i]
total = list_1[0]
if diff < 0:
    diff *= -1
for i in range(len(list_1)):
    help_c = k - list_1[i]
    if help_c < 0:
        help_c *= -1
    if help_c < diff:
        diff = k - list_1[i]
        total = list_1[i]
print(list_1)
print(total)