class Employee:
    #attributes
    company_name="Amazon"
    
    def print_name(self,name):
        print("Employee name = "+name)
    
Employee_1=Employee()

print(Employee_1.company_name)

Employee_1.print_name("Yash")