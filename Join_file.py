
# join

li = ['john ',"cena ",'khali ','randi ','jindermohal ']

for i in li:
    print(i,'and',end=" ")

print("other wwe superstars")

# Another way to join someting 

a = "and".join(li)
print("using join : ",a, "and other wwe superstars")


# maps

numbers = ['3','5','8' ]

for i in range(len(numbers)):  
    numbers[i] = int(numbers[i])   # convert the string into int using for loop

# above code can be written using one-linear using map

numbers1 = list(map(int,numbers))     # convert the list element into integer and then store in a lise
print(f"{type(numbers1)} : {numbers1} \n{type(numbers)} {numbers}")
 
numbers[2] = numbers[2]+1   # 8+1 = 9
print(numbers[2])


def sq(a):
    return a*a

num = [2,4,6,7,8]    
square = tuple(map(sq, num))            # here you can also use lambda fxn : one-linear function
square2 = set(map(lambda x : x*x, num))
print(f"{type(square)} : {square}")
print(f"{type(square2)} : {square2}")


def cube(a):
    return a*a*a

fxns = [sq, cube]    

for i in range(9):
    val = list(map(lambda x: x(i),fxns))
    print(val)


# filter    : return true 

list_1 = [3,5,1,8,8,1,9]


def is_greater_5(x):
    return x>5

gr = list(filter(is_greater_5,list_1))
print("Greater than five :",gr)



# reduce
from functools import reduce


list_2 =[2,4,6,7,8]
num2 = 0

for i in list_2:
    num2 = num2 + i

print("cummulative addition : ",num2)

# above code can be written in one linear

num_reduce = reduce(lambda x,y: x+y,list_2)
print(f"using reduc fxn : {num_reduce}")