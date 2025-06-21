import pandas as pd

df = pd.read_excel('Student_Data.xlsx')

data_science_events = ['Data Visualization using Power BI', 'The SDLC & their transformations']

data_science_attendees = df[
    (df['Events'].isin(data_science_events)) & 
    (df['Attendee Status'] == 'Attending')
]

total_students = len(data_science_attendees)
print(f"Total students who attended Data Science events: {total_students}")