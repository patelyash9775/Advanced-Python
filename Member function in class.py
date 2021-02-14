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
        
    def print_name(self):
        print("Student name: "+self._name)
        
    def increment_age(self):
        self._age=self._age+1
        print("Age for student "+self._name+" is: "+str(self._age))
        
        
student_1=Student("Yash",19,"27/08/2001")
student_2=Student("Nishan",18,"30/06/2001")

student_1.print_name()
student_2.print_name()

student_1.increment_age()
student_2.increment_age()