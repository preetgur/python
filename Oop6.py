# Multiple Inheritance

class Employes:
    no_of_leaves = 8
    var = 10

    def __init__(self,givenname,givensalary):
        self.name = givenname
        self.salary = givensalary

    def print_detail(self):
        print(f"Name of Student is {self.name} and its salary is {self.salary}")

    @classmethod
    def change_no_of_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves
        #change the no of leavesw using class method

    @classmethod
    def method_as_construtor(cls,data):
        return cls(*data.split("-"))

    @staticmethod
    def print_static(string):
        print("This is from Static Method,"+string)    
    @staticmethod
    def print_static_2():
        print("This is second static method :")

##### class second

class Player:
    no_of_game = 5
    var = 20
    game = input("please enter the name of Game : ")
    def __init__(self,name,game):
        self.name= name
        self.game= game

    def print_detail_employe(self):
        print(f"Name of Employee :{ self.name } and it salary is : {self.salary}")

    def print_detail(self):
        print(f"Name of Student is {self.name} and its Game is {self.game}")
        # print(self.salary)   has no attribtue salary

    def print_detail_player(self) :
        return f"From Player : {self.name} and Game : {self.game}"

###### Coolprgrammer class inherit from 'Employes' and 'player' class
# # NOte : order is important       
#  
# class CoolProgrammer(Employes,Player):  it first access the constructor of Employes class

# @@@@ note: if two classes has the same name of varible or fxn then it would use the varible or fxn of the class which is written "first" ex. employes  class varible is used rather than player class

class CoolProgrammer(Employes,Player):

    language = "python"
    
    def print_language(self):
        print(self.language)



preet = Employes("Gurpreet Singh",25000) 
harry = Employes("Harry",120000)

shubham = Player("Shubhum",['cricket'])

karan = CoolProgrammer("KaRAN",20000)  # creating istance of coolprogrammer with respect to constructor of 'employe' class

# karan = CoolProgrammer("KaRAN","Cricket")  # creating istance of coolprogrammer with respect to constructor of 'Player' class

karan.print_detail()   # using the employe class method

karan.print_detail_employe()
print(karan.print_detail_player())

karan.print_language()  # accessing own intance of coolprogrammer class

print(karan.var)