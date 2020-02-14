# Function to create date :

def getdate():
    import datetime
    return datetime.datetime.now()

current_date = getdate()
print(current_date)

# Ask for Log or Retrive Data from file

def log_retrive(user_name):
    user_Log_Retrive = int(input("Enter Your Choice\n Press 1 => Log\n Press 2 => Retrive : "))
    if user_Log_Retrive == 1 :
        print("Log selected : ")
        # function sending the username and selected value
        choice_Excersice_Diet(user_Log_Retrive,user_name)

    elif user_Log_Retrive == 2 :
        print("Retrive selected : ")  
        # function sending the username and selected value
        retrive_Excersice_Diet(user_Log_Retrive,user_name)
  
    else :
        print("Please Select Desired One : ")   

# Choice either Diet or Excercise

def choice_Excersice_Diet(user_Log_Retrive,user_name):
    user_Choice_Diet_Exersice = int(input(" Press 1 => Excersice Log :\n Press 2 => Diet Log : "))

    if user_Choice_Diet_Exersice == 1:
        print("Excersice Selected :")
        ex = "[ Excersice Selected ]"
        name_ex = input("Please Enter The Name of Excersice :")

        with open(user_name+"_"+"Excersice.txt","a") as f:

            f.write("["+str(getdate())+"]  :"+user_name+":"+ex+":"+name_ex+"\n")
        
    elif user_Choice_Diet_Exersice == 2:
        print("Diet Selected :")    
        diet = "[ Diet Selected ]"
        name_diet = input("Please Enter The Name of Diet :")

        with open(user_name+"_"+"Diet.txt","a") as f:
            f.write("["+str(getdate())+"]  :"+user_name+":"+diet+":"+name_diet+"\n")

    else :
        print("Please Select 1 or 2 choice:")   

def retrive_Excersice_Diet(user_Log_Retrive,user_name):
    
    retrive_from_Excersice_Diet = int(input("Which File you want to retrive\n Press 1 => Excersice\n Press 2 => Diet : 2 : "))

    if retrive_from_Excersice_Diet == 1:
        try :
            print("Retrive The Exersice File :")
            with open(user_name+"_"+"Excersice.txt") as f:

                content =f.readlines() 
                #print(content)   for next line use for loop 
                for i in content:
                    print(i,end="")

        except Exception as e:
            print(e)
            print("File is Empty :")
            with open(user_name+"_"+"Excersice.txt","x") as f:
                pass
            
    elif retrive_from_Excersice_Diet == 2:

        print("Retrive The Diet File :")
        try:
            f = open(user_name+"_"+"Diet.txt")
            content =f.readlines() 
            # for next line use for loop

            for i in content:
                print(i,end="")
            f.close()

        except Exception as e:
            # print(e)
            with open(user_name+"_"+"Diet.txt","x") as f:
                pass
            
            print("File is Empty : ")
             
    else :
        print(" Please Enter the Correct No. : ")    

print(" Health Management System :")
user_name = input("Please Enter User Name : ")

if user_name == "Harry":
    print("This is Harry :")
    log_retrive(user_name)
   
elif user_name == "Garry":
    print("This is Garry :")
    log_retrive(user_name)
        
elif user_name == "Larry":
    print("This is Larry :")
    log_retrive(user_name)
       
else :
    print("Something went wrong, Please Enter Correct Name :")

# d2["New Field"] = "New folder Added"   # Added new Key

def signup():
        
    k = 'y'

    while (k is not "n"):
        
        accounts_holder = {}
        name = input("Please Enter Your Name :")
        mobile_no = input("Please Enter Your Mobile No : ")

        accounts_holder["Name"] = name
        accounts_holder["Mobile"] = mobile_no
        accounts_holder["Date"] = current_date.strftime("%c")

        with open("Signup_"+".txt","a") as f:
                    f.write(str(accounts_holder)+"\n")
        
        k = input("ADD MORE : yes /no :")
        print(k)
        continue
    
    retrive_data = input("Do you want to retrive the Data : yes / no : ")

    if retrive_data == "y" :

        import json

        with open("Signup_"+".txt") as f:

                content = f.readlines()
                y = json.dumps(content)

                print(y)

    else :
        print(" Exit ")            

signup()