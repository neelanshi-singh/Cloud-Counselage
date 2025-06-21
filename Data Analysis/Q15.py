import pandas as pd

df = pd.read_excel('Student_Data.xlsx')

#15. Which promotion channel brings in more student participations for the event?

channels = df['How did you come to know about this event?'].str.split(' \| ', expand=True).stack().value_counts()

print(f"Top channel: {channels.idxmax()} with {channels.max()} students")