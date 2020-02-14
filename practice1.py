# Practice Problem : Age calclator

user_input = input("Please Enter Your Age or Year of Bith : ")
current_year = 2020
max_age = 100
max_age_2 = 150

if len(user_input)>2:
    # print("This is year of birth :")
    user_age = current_year-int(user_input)

    if len(user_input) == 3 :
        print("This is also a age :")
        # user_age = current_year-int(user_input)
        print(f"You will be 150 years old after {max_age_2-int(user_input)}")


    if user_age>100:
        print("You seem to be the oldest person alive :")
        print(f"Your Age is : {user_age}")

        print(f"You will be 150 years old after {max_age_2-user_age} years")

    else:
        print(f"Your Age is : {user_age}")
        print(f"You will be 100 years old after {max_age-user_age} years")

elif len(user_input)<3:
    print(f"You will be 100 years old after {max_age-int(user_input)} years")

# elif len(user_input) == 3 and len(user_input)<max_age_2:
#     print("This is also a age :")
#     # user_age = current_year-int(user_input)
#     print(f"You will be 150 years old after {max_age_2-int(user_input)}")

    

else:
    print("Something went wrong !")

user_choice = input("Want to know your age in some exact year :")

if user_choice == 'y':
    print("##############")
    user_age = current_year-int(user_input)

    select_year = int(input("Please Enter Year : "))
    print(f"Current user age is : {user_age}")
    add_age = select_year-current_year
    print(f"In {select_year} your age is {user_age+add_age}")

elif user_choice== 'n':
    print("As your wish! Thanks for visiting the site..") 

else :
    print("someting went wrong!")

    ####### Code with harry ##########
print("########### code with harry ########")    

yearAge = int(input("What is your Age/Year of Birth : "))
isAge = False
isYear = False

# if yearAge<125:
if len(str(yearAge)) == 4:
    isYear = True
else :    
    isAge = True

if (yearAge<1900 and isYear) :
    print("You seem to be the oldest person alive")   

if (yearAge>2019):
    print("You are not yet born")
    exit()

if isAge:
    yearAge = 2019 - yearAge

print(f"you will be 100 years old in {100+yearAge}")

intersetedYear = int(input("Enter the year you want to know : "))
print(f"you will be {intersetedYear-yearAge} years old in {intersetedYear   }")