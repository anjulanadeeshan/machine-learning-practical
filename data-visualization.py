import pandas as pd #working with tables and datasets
import matplotlib.pyplot as plt #creating charts and graphs
import seaborn as sb #colorful and attractive charts

df = pd.read_csv('./student_data_cleaned.csv')
print('cleaned dataset')
print(df)

# plt.figure(figsize=(6, 5))
# #counts how many males and females are in the dataset
# gender_count = df['Gender'].value_counts()
# #create bar charts
# plt.bar(gender_count.index, gender_count.values, color=['skyblue','pink'])
# plt.title('Bar Chart - Count of Gender')
# plt.xlabel('Gender')
# plt.ylabel('Count')
# plt.show()

# plt.figure(figsize=(8,6))
# #create scatter plot
# plt.scatter(df['Age'], df['GPA'], color='purple')
# plt.title('Scatter Plot - Age vs GPA')
# plt.show()

plt.figure(figsize=(8,6))
# Correlation HeatMap

corr = df[['Age', 'GPA', 'Attendance', 'Salary']].corr()
sb.heatmap(corr, annot=True, cmap='coolwarm', center=0, linewidths=0.5)
plt.title('heatmap (correlation)')
plt.show()