# class methods as Alternative construcors

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
        # params = data.split("-")    #parse the string and store into list
        # print(params)
        # return cls(params[0],params[1])
        
        #above thing as one linear
        return cls(*data.split("-"))

preet = Employes("Gurpreet Singh",25000)   # arguments are handle by __init__

print(preet.salary)
preet.print_detail()

diljot = Employes.method_as_construtor("Diljot Singh-9000")
print(f"Name of Student is {diljot.name} and salary is : {diljot.salary} and no of leaves : {diljot.no_of_leaves}")


# static method  : no need of acessing the class varible ans instance varible

# It is creted because we want that only the object of class can access this function only

class Static_class:

    #consturctor
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    # global varibles
    name_of_batch = 2019

    # fxn 
    def details_of_students(self):    
        return(f"Name : {self.name} , Roll no : {self.rollno}")

    @classmethod
    def detail_class(cls, info):
        return cls(*info.split("-"))    

    @staticmethod
    def print_static(data):
        print(f"This data is from static mehod : {data}")  
        return "satic methods "    # store into varibel 


print(" ########### Static Class ########33")
ekbal = Static_class("Ekbal",45)
print(ekbal.name_of_batch)

st = ekbal.print_static("Static Method")     # calling static method
print(st)

gurpreet = Static_class.detail_class("Gupreet-151130")    # create alternative consturctor
print(gurpreet.name,gurpreet.name_of_batch)