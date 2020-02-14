# How to Process command line using argparse

""" 
Two Types of Argument : 
1. Positional  : complsary
2. Optional    : not complsary (--)

"""

"""
key : --y , --operation 
value: 5 ,  add
you can change the order you can put add first then --y

Example : 45 --y 5 --operation add
        : 45 --operation add --y5
45 key[--y] value[5]
"""
# we are writing a program to add,sub,multiply taking input from cmd
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()    #Define varibale and take input
    parser.add_argument("x",help="Enter First Number")      # poisitional argument
    parser.add_argument("--y",help="Enter Second Number")   # optional argument by using --
    parser.add_argument("--operation",help="operation",choices=["add","sub","mul"]) # restrict choices


    args = parser.parse_args()     # value is store in args we can access it 
    print(args.x)
    print(args.y)
    print(args.operation)

# imp : input taking from cmd always in string so convert accordingly   
    n1 = int(args.x)
    n2 = int(args.y)
    result = None

    if args.operation == "add":
        result = n1 + n2
        print("######## Addtion :",result)
    elif args.operation == "sub":
        result = n1 - n2
        print("####### Subtraction",result)

    elif args.operation == "mul":
        result = n1 * n2
        print("####### Multiplication",result)

    else: 
        print(" #### Wrong keyword Entered ####")            


