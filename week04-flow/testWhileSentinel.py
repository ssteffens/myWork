# While loop sentinel controlled
# Author: Stefanie Steffens

val = input("enter something (q to quit):")
while val != 'q':
    print("you said: " + val)
    val = input("(q to quit):")
print ("Goodbye!")