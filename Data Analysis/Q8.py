import pandas as pd

df = pd.read_excel('Student_Data.xlsx')

average = df.groupby("City")["CGPA"].mean()
print(round(average , 2))