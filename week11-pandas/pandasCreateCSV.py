# This program creates a CSV file from a list of data using pandas
# Author: Stefanie Steffens

import pandas as pd

listData = [
    ["John", "math", 23],
    ["John", "programming", 66],
    ["Mary", "math", 45],
    ["Mary", "programming", 33],
    ["Mark", "SIEM", 57],
    ["Mark", "programming", 70],
    ["Mark", "math", 73],
    ["John", "programming", 61]
]

df = pd.DataFrame(listData, columns = ["name", "subject", "grade"])
print(df.head(3))

csvFilename = "grades.csv"
df.to_csv(csvFilename)