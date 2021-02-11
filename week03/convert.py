# This program reads in a float amount of dollars and returns the absolute amount in cent
# Author: Stefanie Steffens

dollarAmount = float(input('Enter the $ amount: '))
centAmount = abs(int(dollarAmount * 100))
print('That amount in cent is: {}'.format(centAmount))