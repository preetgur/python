# Decorator
""" 
Decorators : 
Allows you to wrap one funtion inside another function.
Improve code readability

"""
# you can see if i want to calculte the time i have to write the same code again and again and our main logic is mixed with time logic so this thing can be improve by using decorators
""" 
Function are 'first class objects' in python. 
What it means is that they can be treated just like the other varible and you can pass them as argument to another function or even return them as a return value.

"""

import time

""" 
Procedure how decorators works:

1. First pass (calc_cube) function as argument to decorator function (time_it)
2. Declare second function (wrapper) : which takes the arguments     of (calc_cube) function using *args or **kwargs
3. Then calling the (calc_cube) taking the *args or **kwargs as argument

"""

def time_it(func):                    # calc_cube fxn : as argument to time_it fxn
    print("Decortor",func)       
         
    def wrapper(*args,**kwargs):      #args : (range(1,1000),) kwargs:()
        print("Decortor wraper :",*args,**kwargs)

        start = time.time()            # start : 1245465698
        # def calc_cube(range(1,1000))
        result = func(*args,**kwargs)  # result :[1,8, 27,64 ..]
        # print("Decorator result",result)
        end = time.time(    )          # end : 4546876548
        print(func.__name__+" took "+str((end-start)*1000)+" milli seconds")
        return result

    return wrapper    


def calc_square(numbers):
    start = time.time()

    result = []
    for i in numbers:
        result.append(i*i)

    end = time.time()
    print("calc_square took "+str((end-start)*1000) +" mili sec")
    
    return result

@time_it
def calc_cube(numbers):
    
    result = []
    for i in numbers:
        result.append(i*i*i)
    return result    


if __name__ == "__main__":
    
    array = range(1,10000)
    # print(array.__dir__())
    # for i in array:
    #     print(i)
    out_square = calc_square(array)
    out_cube = calc_cube(array)
