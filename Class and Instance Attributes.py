class Student:
    #attributes
    #1.class attributes
    clg_name="IIT Bombay"
    
    #2.Instance attributes
    def __init__(self,name,age,dob):
        print("Contructor has been called")
        self._name=name
        self._age=age
        self._dob=dob
        
    def print_name(self,name):
        print("Student name: "+name)
        
        
student_1=Student("Yash",19,"27/08/2001")
student_2=Student("Nishan",18,"30/06/2001")

print(student_1._name," ",student_1._age," ",student_1._dob," ",student_1.clg_name)
print(student_2._name," ",student_2._age," ",student_2._dob," ",student_2.clg_name)