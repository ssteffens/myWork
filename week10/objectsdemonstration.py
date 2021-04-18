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
 