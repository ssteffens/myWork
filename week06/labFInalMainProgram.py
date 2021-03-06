# This program imports the module with functions required for lab 6 and then executes the main program
# Author: Stefanie Steffens

import labFinalModule

students = []
choice = labFinalModule.selection()

while (choice != "q"):
    if choice == "a":
       labFinalModule.doAdd(students)
    elif choice == "v": 
       labFinalModule.doView(students)
    elif choice !="q":
        print("\n\nPlease select either a, v or q\n")
    choice = labFinalModule.selection()