import pandas as pd

df = pd.read_excel('Student_Data.xlsx')

#Distribution Of Students Across different graduation years

grad_year_distribution = df["Year of Graduation"].value_counts().sort_index()
print(grad_year_distribution)

