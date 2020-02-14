print("############ while loop ############")

i = 0 
while(i<10):
    i = i+1
    print(i,end=" ")   # end="" use for one linear

print("\n while True")
j =0
while(True):
    print(j,end=" ")
    if(j == 10):
        j +=1
        continue
    elif(j == 15):
        break
    j +=1

while(True):
    no = int(input("\nEnter a Number :"))

    if no>100 :
        print("Congrats you have enterred a number greater than 100")
        break  # comes out of loop
    else: 
        print("Try again")
        continue   


a = input("Enter First Number :")
b = input("Enter second Number :")

# short handy if stmt
if a>b : print(" A B se bda hai")

# short handy if else stmt
print("A B se bda hai") if a>b else print(" B A se bda hai")