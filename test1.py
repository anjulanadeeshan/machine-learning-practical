import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler,MinMaxScaler,LabelEncoder


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
upper_age = 60
lower_age = 18

df['Age'] = np.where(
    df['Age'] > upper_age,
    upper_age,
    np.where(
        df['Age'] < lower_age,
        lower_age,
        df['Age']
    )
)
print(df)

print('--Feature scaling--')
scaler_minmax = MinMaxScaler()
df['Attendance_normalized'] = scaler_minmax.fit_transform(df[['Attendance']]).round(4)

scaler_std = StandardScaler()
df['Salary_standardized'] = scaler_std.fit_transform(df[['Salary']]).round(4)
print(df)

#label encoding
print('--Label Encoding--')

le = LabelEncoder()
df['Department'] = le.fit_transform(df['Department'])
print(df)

#Encoding Categorical Data
df = pd.get_dummies(df, columns=['Gender'], dtype=int)
print("\n---6. After Categorical Encoding ---")
print(df.info())

#save cleaned dataset'

df.to_csv('./student_data_cleaned.csv', index=False)
print("\n Cleaned Dataset saved as 'student_data_cleaned.csv'\n")