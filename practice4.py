# practice problem : Palindrome
''' 
Author : Gurpreet
Date : 14 jan 2020
Purppose : Practice Problem : Palindrome

'''


def next_palindrome(n):
    n = n+1   # increment the numbrer 
    while not is_palindrome(n):   # call the function 
        print(is_palindrome(n))  # returns true or false : if true then it is palindrome
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":

    n = int(input("Please Enter the no of Test Cases : "))
    mylist = []
    for i in range(n):
        mylist.append(int(input(f"Your {i+1} Input : ")))

    print(f"your list : {mylist}")

    for i in range(n):

        print(
            f"Next palidrome for {mylist[i]} is {next_palindrome(mylist[i])}")

    # copy_mylist = mylist[:]  # copy list
    # # copy_mylist = mylist[::-1] # reverse list