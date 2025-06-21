import pandas as pd

df = pd.read_excel('Student_Data.xlsx')

#average CGPA of students
average_cgpa = df["CGPA"].mean()
print(f"Average CGPA: {round(average_cgpa , 2)}")