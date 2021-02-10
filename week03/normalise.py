# This program reads in a string, strips any leading or trailing spaces and converts to lower case
# THe program also outputs the length of the original and the normalised string. 
# Author: Stefanie Steffens

string = str(input('Please enter a string:'))
normalisedString = string.strip().lower()
lenghtString = len(string)
lengthNormalisedString = len(normalisedString)

print('That string normalised is:{}'.format(normalisedString))
print('We reduced the input string from {} to {} characters.'.format(lenghtString, lengthNormalisedString))