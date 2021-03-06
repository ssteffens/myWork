# This program combines the previous lab functions 2-5
# Author: Stefanie Steffens

# Lab 2
def options():
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")

def selection():
    print("What would you like to do?")
    options()
    choice = str(input("Type one letter(a/v/q)")).strip()
    return choice

# Lab 3
def doView(students):
    print(students)

# Lab 4
def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = str(input("Enter name: "))
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

# Lab 5
def readModules(): 
    modules = []
    moduleName = str(input("\tEnter the first module name (blank to quit): ")).strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\tEnter the grade: "))
        modules.append(module)
        moduleName = str(input("\tEnter the next module name (blank to quit): ")).strip()
    return modules


# Main program (Lab 3)

students = []
choice = selection()

while (choice != "q"):
    if choice == "a":
       doAdd(students)
    elif choice == "v": 
       doView(students)
    elif choice !="q":
        print("\n\nPlease select either a, v or q\n")
    choice = selection()
