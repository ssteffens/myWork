# messing around with variable types
# author: Stefanie Steffens

age = 3
print(type(age))

# Type needs to be converted to str so we can concatenate it to the message
print ("type of age is:" + str(type(age)))

# Converting a str to int and int to str
print ("you are " + str(age) )
nextYear = int(age) + 1
print("next year you will be " + (str(nextYear)))