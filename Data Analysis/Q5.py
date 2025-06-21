import pandas as pd

df = pd.read_excel("Student_Data.xlsx")

income_map = {
    "0-2 Lakh": 1.0,
    "2-5 Lakh": 3.5,
    "5-7 Lakh": 6.0,
    "7+ Lakh": 8.0
}

df["Estimated Income"] = df["Family Income"].map(income_map)


average_income = df["Estimated Income"].mean()
print("Estimated Average Family Income (in LPA):", round(average_income, 2))
