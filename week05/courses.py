# This program stores a student name and a list of courses and grades, then prints out the data. 
# Author: Stefanie Steffens

studentData = {
    "name": "Mary", 
    "courses": [
        {
            "courseName": "Programming", "grade": 45,
        }, 
        {
            "courseName": "History", "grade": 99
        }
    ]
}

print("Student: {}".format(studentData["name"]))
for course in studentData["courses"]:
    print("\t {}: \t {}".format(course["courseName"], course["grade"]))
