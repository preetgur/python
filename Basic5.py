print("###### Function ##########")


a = int(input("Enter First Number :"))
b = int(input("Enter second Number :"))

addition = sum((a,b))
print("Sum ( using built in fxn ) : ",addition)

print("###### Simple Function ##########")

def abc():
    print("hello you are in fxn" )

abc()

def xyz(a1,b1):
    print("Addition using fxn :",a1+b1)

w = xyz(a,b)
print(w)

# important concept : return is complusary
print("Important")
def abc2(a1,b1):
    """ This is the function and this is the doc string """
    average = (a1+b1)/2
           # if not return the average it will show the none
    return average
v = abc2(a,b)
print(v)


############# using args
def abc_args(*args):
    """ This is the function and this is the doc string """
    length = len(args)
    print("##### length of args : ",length)

    total = 0
    for i in args:
        total += i
    average = total/length
           # if not return the average it will show the none
    return average
args_value = [4,8,3]
v_args = abc_args(*args_value)
print("########### args function (average) ; ",v_args)



print(abc2.__doc__)

print("###### Try Except ##########")


a1 = input("Enter First Number :")
b1 = input("Enter second Number :")

try:
    print("Try : sum :", int(a1)+int(b7))

except Exception as e :    
    print(e)

print("This line is very important")    