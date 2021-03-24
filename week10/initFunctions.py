# __init__ function
# Author: Stefanie Steffens

class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def fullname(self):
        if hasattr(self, "middlename"):
            return self.firstname + " " + self.middlename + " " + self.lastname
        return self.firstname + " " + self.lastname

    def __str__(self):
        return self.fullname()
    
    def addmiddlename(self, middlename):
        self.middlename = middlename

if __name__ == "__main__":
    person1 = Person("Sebi", "Block")

    print(person1.firstname)
    print(person1.fullname())

    person1.addmiddlename("Joe")

    print(person1)