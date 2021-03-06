# This program reads in modules and grades until the user enters module name as blank
# Author: Stefanie Steffens

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

# Copied from lab4: 

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = str(input("Enter name: "))
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

students = []

doAdd(students)
doAdd(students)
print(students)
