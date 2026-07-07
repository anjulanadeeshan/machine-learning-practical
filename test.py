import pandas as pd

df = pd.read_csv('./employee_data.csv')
print('Description: ', df.describe())
print('Number of rows and columns: ', df.shape)