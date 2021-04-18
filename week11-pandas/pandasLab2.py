# Pandas Lab part 2
# Author: Stefanie Steffens

import pandas as pd
import re
import locale
import matplotlib.pyplot as plt

path = "./data/"
logFileName = path + "access.log"

# 9. Set up column names
colNames = ("ip", "dash1", "userID", "time", "url", "status code", "size of response", "referer", "user agent", "dunno")
df = pd.read_csv(logFileName, sep = " ", header = None, names = colNames)

# 10. Remove columns containing dashes
df.drop(columns = ["dash1", "userID"], inplace = True)

# 12. Check column data types
print(df.dtypes)

# 13. Change the type of the time column to dateTime
df["time"] = pd.to_datetime(df["time"], format = "[%d/%b/%Y:%H:%M:%S]" )

# 14. Get events that happened between two time stamps
start_date = "2021/02/15 23:00"
end_date = "2021/02/15 23:59:59"

# Option 1
#newdf = df.loc[(df["time"] > start_date) & (df["time"] < end_date)]

# Option 2
newdf = df[df.time.between(start_date, end_date)]

print(newdf)

# 15. Get mean amount of data that was downloaded every half an hour
df = df.set_index(["time"])
df.index = pd.to_datetime(df.index, unit = "s")
downloadSamples = df["size of response"].resample(rule = "30min").mean()
print(downloadSamples)

downloadSamples.plot()
plt.show()

#print(df.iloc[0])

