''' 
Author : Gurpreet Singh
date : 14 jan 2020
Description : Palindromify the list
'''

def palindrome(n):

    #second way to select less than 10    
    if n>10:    

        n = n+1
        # while not True:
        while not is_palindrome(n):   # (return) is_palindrome : False / True
            n += 1
    else:
        # n = "##### Your number is less than 10 #### "   
        n = n     
    return n    

def is_palindrome(n):
    return str(n)==str(n)[::-1]
    #it retruns true or false 

if __name__ == "__main__":
    
    n = int(input("Please Enter The Size of list : "))
    mylist = []

    for i in range(n):
        mylist.append(int(input(f"Your {i+1} list items : ")))

    
    # for i in range(n):
    #     print(f"Your Palindrome for  {mylist[i]} is : {palindrome(mylist[i])} ")

    #first way to select less than 10   
    # using list comphresion 
    print(f"Output List : {[mylist[i] if mylist[i]<10 else palindrome(mylist[i]) for i in range(n)] } ")   

    # print([i for i in range(n)])