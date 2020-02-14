# list comprehension

print(f" ######## List [] ########")
numbers = [2,5,6,7,8,1]
even = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)

print("Using simple method:",even,": type : ",type(even))

# Above code can be used in linear

even = [i for i in numbers if i % 2 == 0]
print(f'list comphresion : {even} : type : {type(even)}')

# sqr of numbers

sqr = [ i*i for i in numbers if i%2 == 0 ]
print(f"Square using list comprehsion : {sqr}")


print(" ######## set comphresion {} ######## : Remove Duplicate Numbber ")

s = set([1,3,5,6,7,3,2,1,5])
print(s)


even_set = {i for i in s if i % 2 == 0  }
print(f'Set comphresion : {even_set} : type : {type(even_set)}')

print(" ######## Dict comphresion {} ######## : ")

cities = ["Mumbai","New york","paris"]      # list
countries = ["India","Usa","france"]        # list
 
z = zip(cities,countries)   # imp: zip function returns a tuple
print(z)
for i in z:
    print(i)

d = {"hello"} # set
print(type(d))    

d = {city:country for city,country in zip(cities,countries)}
print(f"Dict using set and list  : {d} : type : {type(d)}")