# simple fxn

def fun(a,b,c,d):
    print("####### Basic Function ########")
    print(a,b,c,d)

fun("Harry","Rohan","Garry","Larry")

# args fxn
print("####### Args Function ########")

# def function(normal , *args , **kwargs) 

#  keep the normal argument First : and *args argument as second , if not then it will show error

# def funargs(*args_Student ,normal_args):  shows error

def funargs(normal_args,*args_Student,**kwargs_Job):
    print(type(normal_args),":", normal_args)

    print("####### Args Function : only add * to parameter and arguments ########")

    print(type(args_Student))  # args take as tuple
    for i in args_Student:
        print(i)

    print("####### Kwargs Function : add ** to parameter and arguments ########")

    print(type(kwargs_Job))
    for key,value in kwargs_Job.items():
        print(F"This is {key} and his profession {value}")   

normal = "This is Normal Arguments"

har = ["harry","Garry","Larry","marry","Preet"]

kw ={"Gurpreet":"web developer","Ekbal":"Web developer","Bhavnit":"Engineer"}


funargs(normal)  # Also run : *args and **kwargs Optional

funargs(normal,*har)

funargs(normal,*har,**kw)  # use  * and **

