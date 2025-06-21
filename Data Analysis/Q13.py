import pandas as pd

df = pd.read_excel("Student_Data.xlsx")

df["Leadership- skills"] = df["Leadership- skills"].astype(str).str.strip().str.lower()

leadership_stats = df.groupby("Leadership- skills")[["CGPA", "Expected salary (Lac)"]].mean()

print("Average CGPA and Expected Salary based on Leadership Experience:")
print(leadership_stats)
