# snake water game
print(" ############ Welcome To The Game : ############")

li = ["snake", "water", "gun"]
import random

i = 0
computer_result = 0
user_result = 0
draw = 0
while(i<=5):

    computer_Choice = random.choice(li)
    # print(choice)

    user_Choice = input("Please Write any of them : \nsnake \nwater \ngun \nEnter here  : ")

    if computer_Choice == user_Choice:
        # print("######### Draw ##########")
        i +=1
        draw = draw + 1
        continue

    elif computer_Choice == "snake" and user_Choice == "water":
        computer_result += 1
        i +=1
        # print("######## computer Wins ############")
        continue 

    elif computer_Choice == "snake" and user_Choice == "gun":
        # print("########### You wins #############")
        user_result +=1
        i +=1
        continue

    elif computer_Choice == "water" and user_Choice == "gun":
        # print("############## computer wins ############")
        computer_result += 1
        i +=1
        continue

    elif computer_Choice == "water" and user_Choice == "snake":
        # print("########### You wins ###########")
        user_result +=1
        i +=1
        continue

    elif computer_Choice == "gun" and user_Choice == "water":
        # print("############ you wins ##########")  
        user_result +=1
        i +=1
        continue

    elif computer_Choice == "gun" and user_Choice == "snake":
        # print("########## computer wins ##########")
        computer_result += 1
        i +=1
        continue

    else:
        print("#########  Something went wrong: ##########")
        i +=1
        continue


def getdate():
    import datetime
    return datetime.datetime.now()

current_date = getdate()
print("Date :",current_date)
if computer_result < user_result :

    print("########## You wins #######")
    print(f"Trial win by user : {user_result}")
    print(f"Trial win by computer : {computer_result}")
    print(f"##### Draw ###### : {draw}")
    
    with open("Snake_Water_Gun"+".txt","a") as f:

        f.write(f"{current_date} : User Wins  : Results: user wins :{user_result} : computer wins :{computer_result}Draw : {draw}\n ")

        

elif computer_result > user_result :
    print("########## Computer wins #######")
    print(f"Trial win by user : {user_result}")
    print(f"Trial win by computer : {computer_result}")
    print(f"##### Draw ###### : {draw}")

    with open("Snake_Water_Gun"+".txt","a") as f:

        f.write(f"{current_date} : Computer wins : Results: user wins :{user_result} : computer wins :{computer_result}Draw : {draw} \n")


elif computer_result == user_result :
    print("##### Match is Draw ########")
    print(f"Trial win by user : {user_result}")
    print(f"Trial win by computer : {computer_result}")
    print(f"##### Draw ###### : {draw}")
    with open("Snake_Water_Gun"+".txt","a") as f:

        f.write(f"{current_date} : Match Draw: Results : user wins :{user_result} : computer wins :{computer_result}Draw : {draw}\n")


else:
    print(" ## something went wrong ##")