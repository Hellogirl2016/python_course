
'''
Найдите сумму цифр трехзначного числа n. Результат сохраните в перменную res.

Пример
n = 123 -> res = 6 (1 + 2 + 3)
n = 100 -> res = 1 (1 + 0 + 0)
'''
print ('Insert 3-digit number')
n = int (input())
print(n)
'''
summa = 0
while a > 0:
    x = a % 10
    summa = summa + x
    a = a // 10
   
   
print(f"summa = {summa}")
'''

res = (n % 10 + (n // 10) % 10 +  (n // 100) % 10)
print(res)


'''
original
n1 = n // 100 # Нахождение первой цифры числа
n2 = (n % 100) // 10 # Нахождение второй цифры числа
n3 = n % 10 # Нахождение третьей цифры числа
res = n1 + n2 + n3
'''