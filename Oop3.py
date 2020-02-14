# class methods
"""  How to change the class varibles?
 
    step 1 : By using the class name it self . for example
            Employes.no_of_leaves = 8
     step 2 : By using the class methods       
"""
class Employes:
    no_of_leaves = 8

    def __init__(self,givenname,givensalary):
        self.name = givenname
        self.salary = givensalary

    def print_detail(self):
        print(f"Name of Student is {self.name} and its salary is {self.salary}")

# taking class as input using "cls"
    @classmethod
    def change_no_of_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

preet = Employes("Gurpreet Singh",25000)   # arguments are handle by __init__

print(preet.salary)
preet.print_detail()

print(preet.no_of_leaves)
print("Leaves Before Updated :",Employes.no_of_leaves)

preet.change_no_of_leaves(54)  # leaves updated and pass new leaves as argument
print("Leaves after Updated :",Employes.no_of_leaves)

Employes.change_no_of_leaves(30) # accessing  using class
print("Leaves after Updated :",Employes.no_of_leaves)
