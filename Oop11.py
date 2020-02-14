# operator overloading and Dunder Methods
# Dunder Methods : starts and ends with  ' __ '

class Employee:
    no_of_leaves = 20

    #Constructor or Dunder Methods
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.age = int(input(f"{self.name}, Please Enter Your Age : "))

    def print_details(self):
        print(f"Name : {self.name}, Age : {self.age} and Salary : {self.salary}")  

    @classmethod
    def class_method(cls,givendata):
        cls.data = givendata      

    @staticmethod
    def static_method(some_string):
        print(f"Text from static method : {some_string}")

# Operator overlaodding  + => __add__ (dunder method)
    def __add__(self,others):
        return self.salary + others.salary


# operator overloading
    def __repr__(self):
        return (f" ##### __repr __ :Dunder method\nEmployee( '{self.name}', {self.salary}, {self.age}) \nName : {self.name}, Age : {self.age} and Salary : {self.salary}")  
        
# __str__ has high priority than __repr__
# __str__ overrides __repr__ unless we call it forcefully 
    def __str__(self):
        return(f"__str__ overrides __repr__ \nName : {self.name}, Age : {self.age} and Salary : {self.salary}")  



emp1 = Employee("Gurpreet",25000)
emp1.print_details()

emp2 = Employee("Ekbal",50000)
emp2.print_details()
print(emp1 + emp2)  # overloadding using Dunder Method : __add__


print(emp1)    # run __str__ method if present if not than run __repr__ method
print(repr(emp1)) # forcefully call repr 

""" Mapping operator to function 
 Example :
  +  => __add__
  /  => __truediv__
  *  => __mul__
"""  
