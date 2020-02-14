# set and frozen sets
"""  
    Set is unordered collection of unique elements. 
    It does'nt allow index operation where as list does.
    Set support taking list as input in the constructor.

"""


basket = {"orange","apple","orange","Apple","mango"}
print(type(basket)," : ",basket)

# second way to create set
a = {}  # It is dictonary not a set
print("###### Type : ",type(a))

a = {"hi"} # It is set
print("###### Type : " ,type(a))

a = set()
a.add("hello")
a.add("How")
a.add("Are")
a.add("You")
a.add(99142)

print(type(a)," : ",a)

# Taking list as input in construcor of set

numbers = [2,3,6,7,7,3,7,9,6]    #list
unique_number = set(numbers)     #set taking list as input
print("List in Set : ",unique_number)

unique_number.add(10)
print("\t\t" ,unique_number)

print("####### Frozen set ")

# frozen set does'nt allow to chanage the content of set .

fs = frozenset(unique_number)
print("Frozen set : ",fs)

# fs.add(10)   # doesn't allow it  :'frozenset' object has no attribute 'add'
print("\t" ,fs)


# basic operation in set
print("####### Basic Operation ")
x ={"a","b","c","d"}

print( "a" in x) 
print( "g" in x) 

for i in x:
    print(i)


y ={"x","b","c","l"}

print("Union : ",x|y)
print("And : ",x&y)        # intersection
print("Difference : ",x-y)

x ={"h","g"}
y ={"a","h","b","g"}
print("Is this a Subset :",x<y)  # is x is a subset of y
 