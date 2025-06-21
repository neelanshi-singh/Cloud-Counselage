import pandas as pd

df = pd.read_excel('Student_Data.xlsx')


#How many unique students in dataset?
unique_students = df.drop_duplicates(subset=["First Name" , "College Name", "Year of Graduation" , "City"])
print("Unique students:", unique_students.shape[0])
