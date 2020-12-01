from Student import Student
from HogwartsGraduate import HogwartsGraduate

# Classes and Objects Practice
student1 = Student("Harry","Gryffindor", 2.9, 15, True)
student2 = Student("Hermione","Gryffindor", 4.0, 15, True)
student3 = Student("Luna","Ravenclaw", 3.5, 14, True)
student4 = Student("Draco","Slytherine", 3.1, 15, False)
student5 = Student("George","Gryffindor", 3.4, 17, False)

graduate = HogwartsGraduate("Fellon", 1995, True)

print(student5.ofAge())
print(student4.ofAge())

#print(graduate.ofAge())
