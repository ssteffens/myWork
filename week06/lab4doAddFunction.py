# This program reads in a student's name, module names and grades using functions
# Author: Stefanie Steffens

students = []

def readModules():
    return()

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = str(input("Enter name: "))
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

doAdd(students)
doAdd(students)
print(students)