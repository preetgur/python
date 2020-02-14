# super() and overriding
# class varible is override by "instance varible "

class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 ="I am inside class A's constructor"
        self.special ="This is special instance variable used with the help of super().__init__"
        self.classvar1 = "Instance var in class A" # instance variable 
        # if we remove the instance varibale 'classvari' then it would use the class variable which comes first

class B(A):
    classvar2 ="I am in class B" # class variabel
    classvar1 = "class B varible "

    # overriding constructor : if instance variabel is not present in constructor then it would not use the constructor of Base class then it will look  for class varible if present

    # But if you wana to use base class construtor then use "super().__init__()"

    def __init__(self):
        super().__init__() # accessing instance variable of base class

        # overrides the instance varible of base class
        self.var1 ="I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        super().__init__() # overrides the above instance variable this class

        print("super : ",super().classvar1) # accessing class variable of : class variable


a = A()
b = B()

print("###############  Attribute override       ##############")
print(b.classvar1)     # instance variable
print(b.classvar2)     # class variable
print(b.var1)          # instance variable
print(b.special)

print("###############  Method override       ##############")
