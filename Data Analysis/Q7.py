import pandas as pd

df = pd.read_excel("Student_Data.xlsx")

courses = df["Quantity"]

# Calculate IQR
Q1 = courses.quantile(0.25)
Q3 = courses.quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

#  Filter outliers
outliers = df[(courses < lower_bound) | (courses > upper_bound)]

print(f"Total outliers in 'Quantity': {len(outliers)}")
print(outliers[["First Name", "Quantity"]])
