#QUE.12) WHICH EVENT TEND TO ATTRACT MORE STUDENTS FROM SPECIFIC FIELDS OF STUDY?
 
import pandas as pd

df = pd.read_excel('Student_Data.xlsx')

most_common_values = df["Events"].value_counts()

N = 20 
print(f"Top {N} most common values in the '{"Events"}' column:")
print(most_common_values.head(N))


