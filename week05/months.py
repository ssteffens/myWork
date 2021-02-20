# This program creates a tuple containing the months of the year. Within the tuple, another tuple is created
# just using the summer months. The program then prints the summer months one by one. 
# Author: Stefanie Steffens

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
"November", "December")

summerMonths = months[4:7]

for month in summerMonths:
    print(month)