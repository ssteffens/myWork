# Lab week 11
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

# 2. Describe dataset
print(df.describe())
print(type(df.describe()))

# 3. Create csv file
path = "./data/"
csvFilename = path + "grades.csv"
df.to_csv(csvFilename)

# 4. Create Excel file
excelFileName = path + "grades.xlsx"
df.to_excel(excelFileName, index = False, sheet_name = "data")

# 5. Add description to another sheet called summary
#with pd.ExcelWriter(excelFileName, engine = "openpyxl", mode = "a") as writer:
#    df.describe().to_excel(writer, sheet_name = "summary")

# 6. Calculate and print mean of the grades
mean = df["grade"].mean()
print(mean)