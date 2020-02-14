
print(" ######################### Welcome To The Game #######################")

# Exercise - Game : Guess The No

i = 0 
total_guess = 5
print("     ###################Total No of Guess : ",total_guess,"####################")

while(i<total_guess):
    
    number = int(input("Please Enter the No : "))
    target_value = 25
    
    if number>target_value:

        print("Your Guess Number is High :  Try Again")
        i += 1
        print("*************Remaining Guess :",total_guess-i)

        if i>=5:
            print( "***High***** Game over ******High******")

        continue
    elif number<target_value:
        print("Your Guess Number is Low :  Try Again")
        i += 1
        print("**********Remaining Guess :",total_guess-i)
        if i>=5:
            print( "****Low**** Game over ******Low*****")

        continue
    elif number == target_value:
        print("Your Guess is Right :  !Winner Winner Chicken Dinner ")
        i += 1
        print("****** You Win on :",i, " Guess **********")

        break
    elif i >=5 :
        print(" *********** Game over *************")

    
        
# Pattern

print(" ########### Create Patterns  ############")

no = int(input("Please Enter the no. of rows you want : "))
choice_pattern = int(input("Please enter 0 for ascending order , enter 1 for descending order : "))
j=0

if choice_pattern == 0:
    for i in range(1 ,no+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif choice_pattern == 1:
    for i in range(no,0,-1):
        for j in range(1, i+1):
            print("*",end=" ")
        print()    
else :
    print("Please select the desired one : ")        
