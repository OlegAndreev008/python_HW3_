# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
list_1 = []
count_el = 0
k = int(input("введите значение эл-та: "))
count = int(input("сколько эл-тов будет в массиве: "))
for i in range(count):
    el = int(input(f"значение {i + 1} эл-та: "))
    list_1.append(el)
    if k == list_1[i]:
        count_el += 1
print(list_1)
print(count_el)
