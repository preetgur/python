# setter and property Decorators

class Employee: 
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{fname}.{lname}@codewith.com"

    def explain(self):
        return f"First Name : {self.fname}, Last Name : {self.lname}"   
# @property decorator : is used to convert fxn into property        
    @property
    def print_email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set"
        return f"{self.fname}.{self.lname}@codewith.com"
        
    @print_email.setter 
    def print_email(self,string):
        print("Setting now ..")
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]  

    @print_email.deleter
    def print_email(self):
        self.fname = None
        self.lname = None

obj1 = Employee("Gurpreet","Singh")
obj2 = Employee("Ekbal","Singh")

print(obj1.explain())

print(obj1.email)

# If we wanna to change first name of email it would not be abel to change because when we initialize the object then we write first name  it as "gurpreet"  Ex. like

obj1.fname = "Ekbal"     # change name : but not applicable
print(obj1.email)

# print(obj1.print_email())  # function

print(obj1.print_email)  # it change the first name : using property


# setter : when we can't set attribute then use it

obj1.print_email = "mr.gurpreet@gmail.com" # AttributeError: can't set attribute use setter property

print(f"First Name :{obj1.fname} and Last Name : {obj1.lname}")


del obj1.print_email # AttributeError: can't delete attribute : create deleter
print(f"First Name :{obj1.fname} and Last Name : {obj1.lname}")
print(obj1.print_email)


# object introspection : information of object

print("####### Object Introspection")
skillf = Employee("Skill","F")
# print(skillf.email)
print(type("hello"))
print(type(skillf))
print(id(skillf))
print(dir(skillf))

import inspect
print(inspect.getmembers(skillf))

print(inspect.isclass(Employee))
