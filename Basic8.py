print(" Scooping in Python : Local Global")

i = 10   # Global variable

def function1():
    i = 5 # local variable
    j = 6
    print("Inside the Function : ",i,j)

function1()
print("Outside the function : ",i)

print("########## how to change the Global variable : using global keyword : ########")


k = 10   # Global variable

def function2():
    # k = 5 # local variable  
    # NameError: name 'K' is not defined  : This can be resloved by using "global k = k+5"  
    # k = K+5    
    global k 
    k=k+5              
    j = 6
    print("Inside the Fun : ",k,j)

function2()
print("Outside the function : ",k)

print("####### IMPORTANT Tips ############")

# When we call the fxn it will show error that  NameError: name 'l' is not defined : 
# Because when we use golbal keyword it search the varible outside the functions but we declared the varible inside the fxn : in order to resolve the error we have to declared the varible outside the fxn

l = 5
def abc():
    # l = 10   # global keyword ignore this  l=10
    def xyz():  # nested fxn
        global l
        print(f"Befor update the value : {l}")
        l = l+25

    print("Before calling the xyz() : ",l)
    xyz()    
    print("After calling the xyz() : ",l)

print("Before calling the abc() value of l :",l) 
abc()   
print("After calling the abc() Updated value of l :",l)



print("########## Recursion ################")

# Rescrsion : using fxn inside the fxn

def factorial_iterative(user_input):

    fac = 1
    for i in range(user_input):
        fac = fac * (i+1)
    return fac    
    # print(fac)

user_input = int(input("Enter the Number for which do you want factorial : " ))

ans = factorial_iterative(user_input)            # calling the functions
print("Factorial using iterative method : ",ans)




def factorial_recursion(user_input):

    if user_input == 1 :
        return 1
    else :
        return user_input * factorial_recursion(user_input-1)    

user_inp = int(input("Enter the Number for which do you want factorial : " ))

an = factorial_recursion(user_inp)
print("Factorial using factorial_recursion method : ",an)

#  return 5 * factorial_recursion(4)
#  return 5 * 4 * factorial_recursion(3)
#  return 5 * 4 * 3 * factorial_recursion(2)

# Quiz : Create a Fibonacci series


n = int(input("Enter the First Fibonacci No :"))


def fibonacci(n):
    
    if n == 0 :
        return 0

    elif n == 1: 
        return 1   
    else :
        return fibonacci(n-1)+fibonacci(n-2)    

result = fibonacci(n)
print("Fibonacci Series  : ",result)



print(" ########## Lambda Functions / anonymous / one linear fxn  ############")

first_value = int( input("Enter First No : "))
second_value = int ( input("Enter Second No : "))

def minus(x,y):
    return x-y

mi = minus(first_value, second_value)
print("Subtraction using Simple fxn: ",mi)

# Replacement to above problem 

sub = lambda x,y : x-y
print("Subtraction  using Lambda : ",sub(first_value,second_value))

# Sorting list

li = [ [4,6],[1,2],[0,44],[9,2]]    # list of list

li.sort()           # key= taking as a function 
                                    # lambda x:x[0]  : return 0 index value and sort accordingly
print("Sorting list [Default] : ",li)

li.sort(key=lambda x: x[0])
print("Sorting list Based on first element in list : ",li)


li.sort(key=lambda x: x[1])
print("Sorting list Based on second elment in list : ",li)
