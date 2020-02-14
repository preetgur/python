# Abstraction and Encapsulation

# Encapsulation : hides Details
# Abstraction :  divide into pieces each layer 
#  Abstraction means displaying only essential information and hiding the details

# single inheritance


class Employes:
    no_of_leaves = 8

    def __init__(self,givenname,givensalary):
        self.name = givenname
        self.salary = givensalary

    def print_detail(self):
        print(f"Name of Student is {self.name} and its salary is {self.salary}")

# taking class as input using "cls" : cls = Employes (Name of class)
    @classmethod
    def change_no_of_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

# class method as alternative constructor

    @classmethod
    def method_as_construtor(cls,data):
    
        return cls(*data.split("-"))

    @staticmethod
    def static_fxn():
        print("This is static")    


# Single inheritance : inherit the features of Empoyes class

class Programmer(Employes):

    no_of_leaves = 20

    def __init__(self,givenname,givensalary,language):
        self.name = givenname
        self.salary = givensalary
        self.language = language

    def print_prog(self):
        return f"The Programmer's Name : {self.name} and salary : {self.salary}"

    def user_print(self,info):
        self.info = info
        return f"Extended : {self.info} ,{self.name}, {self.salary} "      

preet = Employes("Gurpreet Singh",25000)   # arguments are handle by __init__

print(preet.salary)
preet.print_detail()

diljot = Employes.method_as_construtor("Diljot Singh-9000")
print(f"Name of Student is {diljot.name} and salary is : {diljot.salary} and no of leaves : {diljot.no_of_leaves}")


shubham = Programmer("Shubham",10000,['python'])
karan = Programmer("karan",20000,['Javascript'])
print("######## Using Inheritance ")
print(shubham.name)
print(f"Name : {karan.name}, Salary : {karan.salary} and No of leaves : {karan.no_of_leaves} , {karan.language}")

print(f" From Programmer : {shubham.print_prog()}")
print(shubham.user_print("hi"),shubham.no_of_leaves)

print(f"No. of leaves from Parent class : {preet.no_of_leaves}\nNo.of leaves from Programmer class : {shubham.no_of_leaves}")
# print(f" From Programmer : {shubham.user_print()}")
