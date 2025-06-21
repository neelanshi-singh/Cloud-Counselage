import pandas as pd

df = pd.read_excel("Student_Data.xlsx")

avg_gpa_by_college = df.groupby("College Name")["CGPA"].mean()

top_5_colleges = avg_gpa_by_college.sort_values(ascending=False).head(5)

print("Top 5 Colleges by Average CGPA:\n")
print(top_5_colleges)
