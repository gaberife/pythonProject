class Student:
    #Classes and Objects Practice
    def __init__(self, name, house, gpa, age, inDA):
        self.name = name
        self.house = house
        self.gpa = gpa
        self.age = age
        self.inDA = inDA
    def ofAge(self):
        if self.age >= 17:
            return True
        else:
            return False

    def getAge(self):
        return self.age