# Diamond shape problem in Multiple Inheritance

class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    pass
    def met(self):
        print("This is a method from class B")


class C(A):
    def met(self):
        print("This is a method from class C")


class D(B,C):
    def met(self):
        print("This is a method from class D")


a = A()
b = B()
c = C()
d = D()

d.met() 
#It first check the met() fxn in class D if not found then in class B if not found then in class C not found then in class A

# class D => class B => class C => class A