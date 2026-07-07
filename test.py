import pandas as pd

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
print(df)