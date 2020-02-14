
print("How to use print stmt in python")

"""  this a Doc String """

# This is comment in Python
r ="This is basic.py file varible "
print("c:\n harry")   # \n => next line

print("c:\'harry")   # \' => use colon '

print(3 * "hello world \n")

a = "45"  # String not a number
b =  5

print(type(a))
print(int(a)+b)

print("Take input from user")

name = input("Please Enter your name : ")   #  By default it Store the data as string  we have to typecast as required
print(name)

print("Adding Two Numbers ")
x = input("Enter First Number : ")
y = int(input("Enter Second Number : "))  # One way to typecast  the string into integer

print("Sum of Two number : ",int(x)+y)   # Second way to typecast the string

print("How to calculate the length of string and how to use slicing :")

message = "Gurpreet is a good boy"
print("Length of message : ",len(message))
print("One way to slicing : ", message[:20])   # nameOfString[startingindex:Endingindex: increment]
print("Second way to slicing : ", message[5:])
print("Third way to slicing : ", message[0:21:2])
print("Fourth way to slicing : ", message[:])   # print all the elements
print("Fifth way to slicing [negative] : ", message[-10:-1])  # using negative way
print("Sixth way to reverse slicing [negative] : ", message[::-1])  # Reverse the String




