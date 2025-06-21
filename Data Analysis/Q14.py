import pandas as pd 

df = pd.read_excel('Student_Data.xlsx')

#14. How many students are graduating by the end of 2024?

graduates_2024 = df[df["Year of Graduation"] <= 2024]

count = graduates_2024.shape[0]

print(f"Number of students graduating by end of 2024: {count}")
