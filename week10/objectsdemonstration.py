# Objects
# Author: Stefanie Steffens

class Nameofclass: 
    name = ""
    last = ""
    def getfullname(self):
        return self.name + " " + self.last

inst = Nameofclass()
inst2 = Nameofclass()

inst.name = "Andrew"
inst2.last = "Beatty"
person = inst

print(person.getfullname())

str1 = "blah"
str2 = str1
str1 += "with bells on top"

print(str2)