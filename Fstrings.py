# F Strings

me = "Gurpreet "
a1 = 4
a = " This is %s" %me
print(a)

a = "This is %s %s" %(me, a1)
print(a)

a = " This is {} {}"
b = a.format(me,a1)
print("Using format fxn : ",b)


a = " This is {1} {0}"
b = a.format(me,a1)
print("Using format fxn with indices : ",b)


# f strings 
import math
print("######## F strings : ########")

a = f"This is {me} {a1} : multiplication{4*6} {math.cos(65)}"
print(a)