# This program analyses the grades.csv file
# Author: Stefanie Steffens

import pandas as pd
import matplotlib.pyplot as plt

filename = "grades.csv"

df = pd.read_csv(filename, index_col = 0)
df.dropna(inplace = True)                   # removes blank values; not removing them in actual data file
df.drop_duplicates(inplace=True)            # removes duplicates; not removing them in actual data file
#print(df)

df = df.pivot_table(values = "grade", index = ["name", "subject"], aggfunc = "max").reset_index()
print(df)

meanSubject = df.groupby("subject").mean()   # calculates average, grouped by subject 
#print(meanSubject)

meanStudent = df.groupby("name").mean()      # calculates average, grouped by name 
#print(meanStudent)


df = df.pivot(index = "name", columns = "subject", values = "grade")
print(df.corr())                            # correlation between subjects
df.plot.bar()
plt.show()
