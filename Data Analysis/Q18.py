#QUE.18)HOW MANY STUDENTS KNOW ABOUT THE EVENT FROM THEIR COLLEGES?WHICH OF THESE TOP 5 COLLEGES?

import pandas as pd
data = pd.read_excel('Student_Data.xlsx')

college_counts = data['College Name'].value_counts().reset_index()

college_counts.columns = ['College Name', 'Events']


college_counts = college_counts.sort_values(by='Events', ascending=False)


top_5_colleges = college_counts.head(5)

print("Top 5 Colleges with the Most Students:")
print(top_5_colleges)