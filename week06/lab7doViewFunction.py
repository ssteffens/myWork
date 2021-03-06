# This program adds the doView() function to the combined program (lab 6)
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

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = str(input("Enter name: "))
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

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

# New functions: 
def displayModules(modules):
    print("\tName   \t\tGrade")
    for module in modules: 
        print("\t{} \t{}".format(module["name"], module["grade"]))

def doView(students):
    for currentStudent in students: 
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])

# Main program 

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