
"""
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
"""
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())

list_d = list(data['whoAmI'])
for j in range(len(list_d)):
    if list_d[j] == 'robot':
        list_d[j] = 0
    else:
        list_d[j] = 1
res = pd.DataFrame({'whoAmI':list_d})
print(list_d)
print(res)
