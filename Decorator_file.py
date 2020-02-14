def function1():
    print("subscribe now")

fun2 = function1  # makes fxn copy
fun2()          # print subscribe now 

del function1
fun2()          # print subscribe now


# ####### we can also return the function 

def func_return (num):
    if num == 0:
        return print

    if num==1:
        return sum    

a = func_return(1)
print(a)

# ####### we can also  pass the fxn as argument

def executor(func):

    func("This")    # isame as : print("This")

executor(print)      # passing the 'print' fxn as arguments


# ####### decorators
print("############ Decorators ")

""" 
In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.


In Python, functions are the first class objects, which means that –

Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.

Functions can be defined inside another function and can also be passed as argument to another function.

"""

def hello_decorator(func1) :
    def now_exec(c):
        print("Exceuting now")

        func1(c)  # external function calling

        print("Executed")

    return now_exec    


@hello_decorator
def function_to_be_used(c):
    print("output from external function :",c)

# abc = ded1(external_fun)   # This line is also written as using the "@" above the function

# abc()

if __name__ == "__main__":
    function_to_be_used("hello")  # in case when use @