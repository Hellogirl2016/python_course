"""
Дан файл california_housing_train.csv. Определить среднюю стоимость дома ,
где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
Используйте модуль pandas.
"""


import pandas

data = pandas.read_csv('california_housing_test.csv')
new_data = data[data['population'] < 500]['median_house_value']
avg = new_data.mean()
print(avg)

"""
original
import pandas as pd

df = pd.read_csv('california_housing_train.csv')
avg = df[(df['population'] > 0) & (df['population'] < 500)]['median_house_value'].mean()  # Средняя стоимость дома, где количество людей от 0 до 500


"""