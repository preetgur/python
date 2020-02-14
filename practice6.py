"""
Author : Gurpreet Singh
Date : 14 jan 2020
Purpose : Guess the Number

 """
# import random

# starts = int(input("Enter The Starting range Number : "))
# ends = int(input("Enter the End range number : "))

# # print(dir(random))
# rand = random.randint(starts,ends)   # inculding both end points
# # rand = random.randrange(starts,ends)
# print(rand)

# count_first = 0
# count_second = 0
# status = True
# while status:
#     first_player = int(input("First Player Turn : "))

#     if first_player == rand:
#         count_first +=1
#         print(f"Total counts : {count_first}")
#         status = False

#     elif first_player>rand:
#         count_first +=1
#         print("Your Guess Number is Greater :")    

#     elif first_player<rand:
#         count_first +=1
#         print("Your Guess Number is Smaller :")    
    
# print("#####################")
# rand = random.randrange(starts,ends)
# print(f"Second Player : {rand}")

# status2 = True
# while status2:
#     second_player = int(input("Second Player Turn : "))

#     if second_player == rand:
#         count_second +=1
#         print(f"Total counts : {count_second}")
#         status2 = False

#     elif second_player>rand:
#         count_second +=1
#         print("Your Guess Number is Greater :")    

#     elif second_player<rand:
#         count_second +=1
#         print("Your Guess Number is Smaller :")    

# if count_first>count_second:
#     print(f"Second Player is winner :")

# elif count_first<count_second:
#     print(f"First Player is winner : ")

# else:
#     print("Tie")


""" 
rand = random.randint(starts,ends)   # inculding both end points
rand = random.randrange(starts,ends)
"""

def guessGame(a,b,rand):
    guess = int(input(f"Guess a number btw {a} and {b} : "))
    no_gues = 1
    while  guess!= rand:
       
        if guess < rand:
            guess = int(input(f"Enter a bigger number : "))
            no_gues += 1

        else :
            guess = int(input(f"Enter a smaller number : ")) 
            no_gues += 1   

    print(f"You guessed the number in {no_gues} times")
    return no_gues


if __name__ == "__main__":
    import random
    a = int(input("Enter the value of a : "))
    b = int(input("Enter the value of b : "))
    rand = random.randint(a,b)
    print(f"###### {rand}")
    print(f"Player 1 Turns : ")
    g1 = guessGame(a,b,rand)

    print(f"Player 2 Turns : ")
    rand2 = random.randint(a,b)
    print(f"###### {rand2}")
    g2 = guessGame(a,b,rand2)

    if g1<g2:
        print(f"Player 1 wins")
    elif g1>g2:
        print(f" Player 2 wins")
    else:
        print("######### Tie ###########")    

    print(f"Payer 1 Answer is {rand} and Player 2 Answer is {rand2}")    