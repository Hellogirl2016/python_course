"""
Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

Пример:


list_1 = [1, 2, 3, 4, 5]
k = 6
# 5
"""
list_1 = [1, 2, 13, 4, 5]
k = 10
b = list_1[0]
min = abs(k - list_1[0]) 

for i in range(0, len(list_1)):
    a = abs(k - list_1[i])
    if a < min:
        min = a
        b = list_1[i]
print(b)
    
    """
    m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)
    """
    
        
        
    