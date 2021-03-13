# This program reads in student details, outputs them and adds an option to save the data. 
# Author: Stefanie Steffens

def options():
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(q) Quit")

def selection():
    print("What would you like to do?")
    options()
    choice = str(input("Type one letter(a/v/s/q)")).strip()
    return choice

def doView(students):
    print(students)

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = str(input("Enter name: "))
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

def doSave(students):
    print("in save")

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


# Main program

students = []
choice = selection()

while (choice != "q"):
    if choice == "a":
       doAdd(students)
    elif choice == "v": 
       doView(students)
    elif choice =="s":
        doSave(students)
    elif choice !="q":
        print("\n\nPlease select either a, v or q\n")
    choice = selection()
