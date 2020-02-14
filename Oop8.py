# Public,Private,Protected Access Speifier
"""
Public - availabe to all class
Protected - availabel to child(subclass) class only
Private - availabe within its own class
"""

class Employes:
    no_of_leaves = "Public"  # public
    _protect = "Protected Varible"
    __privat = "Private Varible"

    def __init__(self,givenname,givensalary):
        self.name = givenname
        self.salary = givensalary

    def print_detail(self):
        print(f"Name of Student is {self.name} and its salary is {self.salary}")

    @classmethod
    def change_no_of_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

preet = Employes("Gurpreet Singh",25000)  

print(preet.no_of_leaves)    # calling public variable
print(preet._protect)   # calling protected varible
print(preet._Employes__privat)   ## calling private varible


####### Polymorphism : ability to take more than one form 

print(5+6)
print("5"+"6")