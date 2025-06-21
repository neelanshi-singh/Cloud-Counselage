import pandas as pd

df = pd.read_excel('Student_Data.xlsx')

filtered_df = df[(df['CGPA'] >= 8.0) & (df['Experience with python (Months)'] >= 5)]


avg_salary = filtered_df['Expected salary (Lac)'].mean()

print(f"Average expected salary for students with high CGPA (≥ 8.0) and more Python experience (≥ 5 months): {avg_salary:.2f} lakhs")