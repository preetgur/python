class Student:
    pass


garry = Student()                    # creating obect of class 
larry = Student()


# instance variable
garry.name = "Garry"
garry.std = 12
garry.section = 1

print("Standard of garry :",garry.std)


class Employee :
    
    no_of_leaves = 8  # same for all objects
    pass

preet = Employee()
harry = Employee()

preet.name = " Gurpreet Singh "
preet.salary = 150000

harry.name = " Harpreet Singh "
harry.salary = 250000

print("Salary of harry : ",harry.salary)
print("Salary of Preet : ",preet.salary)

print("NO of leaves by preet : ",preet.no_of_leaves)
print("NO of leaves by harry : ",harry.no_of_leaves)
print("no of leaves by Class : ", Employee.no_of_leaves)

Employee.no_of_leaves = 5   # change by  using class
print("no of leaves after changing : ", Employee.no_of_leaves)

harry.no_of_leaves = 6   # it creates a new instance varialbe  in harry with "no_of_leaves"
print("NO of leaves by harry : ",harry.no_of_leaves)
print("no of leaves after changing : ", Employee.no_of_leaves)

print(preet.__dict__)
print(harry.__dict__)   # added new instance : no_of_leaves


print(Employee.__dict__)


# we cannot change the class varible by using the instance variable