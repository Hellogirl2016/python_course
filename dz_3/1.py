"""
Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

Найдите количество и выведите его.

Пример:


list_1 = [1, 2, 3, 4, 5]
k = 3
# 
"""
list_1 = [1, 2, 3, 4, 5]
k = 3
count = 0

for el in list_1:
    if el == k:
        count += 1
print(count)

"""
count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)
"""