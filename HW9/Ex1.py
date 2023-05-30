
import pandas as pd

df = pd.read_csv ('california_housing_train.csv')

print(df.head())

#Типы данных в таблице
print(df.dtypes)

# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
print(df[df['population'] < 500][['median_income']])

# Задача 42: Узнать какая максимальная households в зоне минимального значения population
df1 = df.loc[df.population < df.population.quantile(.25)]
print(df1.households.max())