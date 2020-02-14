#    self and __int__

class Employee : 
    no_of_leaves = 0
    
    # self represent : the name of "object"

    def __init__(self,given_name,given_salary):  #constructor

        self.name = given_name
        self.salary = given_salary

    # self represent : the name of "object".attribute

    def print_details(self):
        return f"Name is {self.name} and Salary is {self.salary}"

    def change_details(self):

        change_name = input("Please enter new name :")
        self.name =  change_name   
        return f"Name is {self.name} and Salary is {self.salary}"


preet = Employee("Gurpreet Singh",25000)   # arguments are handle by __init__
print(preet)

print(preet.salary)
print(preet.print_details())
print(preet.change_details())
# harry = Employee()

# preet.name = " Gurpreet Singh "
# preet.salary = 150000

# harry.name = " Harpreet Singh "
# harry.salary = 250000

# print("Salary of harry : ",harry.salary)
# print("Salary of Preet : ",preet.salary)

# harry_details = harry.print_details()

# print(harry_details)
