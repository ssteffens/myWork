# This program prints out a menu of commands then confirms the command entered by the user
# Author: Stefanie Steffens

def options():
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")

def selection():
    print("What would you like to do?")
    options()
    choice = str(input("Type one letter(a/v/q)")).strip()
    return choice
    

choice = selection()
print("You chose {}".format(choice))