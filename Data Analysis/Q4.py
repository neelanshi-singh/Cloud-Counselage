import pandas as pd

df = pd.read_excel('Student_Data.xlsx')

#Distribution Of Students Across different graduation years

python_experience_distribution = df["Experience with python (Months)"].value_counts().sort_index()
print(python_experience_distribution)

