print(' IF ELSE STMT')

a = input("Enter First Number :")
b = input("Enter second Number :")

# short handy if stmt
if a>b : print(" A B se bda hai")

# short handy if else stmt
print("A B se bda hai") if a>b else print(" B A se bda hai")
if a>b:
    print("First Number is Greater")        

    # If a>b then following operation is performed based on the user input
    print("Enter the name of operation or enter symbol")

    fxn = input("Operation Performed : Add / Sub / Multiply :")
    if fxn =='+' or fxn == 'Add' :
        print("Addition :",int(a)+int(b) )
    elif fxn =='-' or fxn == 'Sub':
        print("Subtraction :",int(a)-int(b) )
    elif fxn == "*" or fxn == 'Multiply':
        print("Multification :",int(a)*int(b) )
    else :
        print("Divide : ",int(a)/int(b))    

elif a == b:
    print("Both Number is Equal")       
else :
    print("Second Number is Greater")     

print("###############################################")

list1 = [3,45,6,2,1]

if 45 in list1:
    print("yes it's in the list")


if 46 not in list1:
    print("No it's in the list")    

print(2 in list1)                  # Return True
print(45 not in list1)             # Retrun false because 45 is in the list


print("######################  Quiz  ####################")
#Design a calucalutor which will correctly solve all the problems except the following one:
#  45*3=555 , 56+9=77 56/6 =4

x = int(input("Enter First Number : "))
y = int(input("Enter Second Number : "))
fxn = input("Operation Performed : Add / Sub / Multiply : ")

if x == 56 and y == 9 and fxn == '+':
    print("56+9 : 77")        
elif fxn =='+' or fxn == 'Add' :
    print("Addition :",int(x)+int(y) )
elif x == 45 and y == 3 and fxn == '*':
    print("45*3 : 555")        
elif fxn =='-' or fxn == 'Sub':
    print("Subtraction :",int(x)-int(y) )
elif fxn == "*" or fxn == 'Multiply':
    print("Multification :",int(x)*int(y) )

else :
    print("Divide : ",int(x)/int(y))    


print("################ for loop ####################")

list2 =[1,2,"Gurpreet",4,[2,5,3,"GArry",1],["preet",2]]

# one way to iterate
for i in list2:
    print(i)

print("################ Second way to iterate [List of List ]####################")

list3 =[ ["harry",1] , ["Larry",6], ["garry", 9], [4,6]] # list indices must be integers or slices, not tuple

for i,j in list3:
    print(i,"has value",j)    

print(" ###### convert list into dictionary #####")

dict1 = dict(list3)
print(dict1)

for i,j in dict1.items():
    print("List of Keys",i,"and value ",j)

# for i in dict1:
#     if str(dict1).isnumeric and i>6:
#         print(i)