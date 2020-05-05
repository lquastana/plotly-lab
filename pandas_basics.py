import pandas as pd
import numpy as np
df = pd.read_csv('salaries.csv')


print(df[['Name','Salary']])



print(df['Salary'].min())
print(df['Salary'].max())
print(df['Salary'].mean())

filter_age = df['Age'] > 30
print(df[filter_age])


print(df['Salary'].unique())

print(df.columns)

print(df.info())

mat = np.arange(0,10).reshape(5,2)
print(mat)
df = pd.DataFrame(data=mat,columns=['A','B'])
print(df)