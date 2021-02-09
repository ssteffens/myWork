# Using the type() function to check variable types
# Author: Stefanie Steffens

i = 3
fl = 3.5
isa = True
memo = "how now Brown Cow"
lots = []

print('variable i is of type: ' + str(type(i)) + ' and value: ' + str(i))
print('variable fl is of type: ' + str(type(fl)) + ' and value: ' + str(fl))
print('variable is is of type: ' + str(type(isa)) + ' and value: ' + str(isa))
print('variable memo is of type: ' + str(type(memo)) + ' and value: ' + memo)
print('variable lots is of type: ' + str(type(lots)) + ' and value: ' + str(lots))

#Cleaner version: 
print('variable {} is of type: {} and value: {}'.format('i', type(i), i))
print('variable {} is of type: {} and value: {}'.format('fl', type(fl), fl))
print('variable {} is of type: {} and value: {}'.format('is', type(isa), isa))
print('variable {} is of type: {} and value: {}'.format('memo', type(memo), memo))
print('variable {} is of type: {} and value: {}'.format('lots', type(lots), lots))