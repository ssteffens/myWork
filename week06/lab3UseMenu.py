# This program keeps displaying the menu (lab2) until the user picks q.
# If the user picks a, a function called doAdd() is called, if the user
# picks v, then a function called doView() is called
# Author: Stefanie Steffens

# Functions copied from lab2:

def options():
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")

def selection():
    print("What would you like to do?")
    options()
    choice = str(input("Type one letter(a/v/q)")).strip()
    return choice

# New functions: 
def doAdd():
    print("in adding\n")

def doView():
    print("in viewing\n")


choice = selection()

while (choice != "q"):
    if choice == "a":
       doAdd()
    elif choice == "v": 
       doView()
    elif choice !="q":
        print("\n\nPlease select either a, v or q\n")
    choice = selection()

