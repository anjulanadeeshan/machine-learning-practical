import pandas as pd
import numpy as np

df = pd.read_csv('./student_data.csv')
print('Description: ', df.describe())
print('Number of rows and columns: ', df.shape)
print('--handle inconsistant of data--')
print()

df['Gender'] = df['Gender'].str.lower().str.strip().str.replace(" ","")
gender_map = {'male' : 'Male', 'female' : 'Female', 'f': 'Female', 'm':'Male'}

df['Gender'] = df['Gender'].map(gender_map)
print('formatting standarized')
print(df)

print('--Fix incorrect datatypes--')
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Department'] = df['Department'].replace('0',np.nan)
print(df)

print('--Handling Missing Values--')
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].mean()).round(2)
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])

#fillina - :fill missing values -> replace NaN with another value
#mode()[0] - first mode value

print(df)

print('---Handling noisy values---')
df['Department'] = df['Department'].replace('Computer Since','Computer Science')
print(df)

print('--Handling Outliers--')
upper_limit = 60000
lower_limit = 30000

df['Salary'] = np.where(
    df['Salary'] > upper_limit,
    upper_limit,
    np.where(
        df['Salary'] < lower_limit,
        lower_limit,
        df['Salary']
    )
)

print(df)