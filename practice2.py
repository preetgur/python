# Practice problem 2 : Divide the apples

try :
    n = int(input("Please Enter the Number of Apples Harry got  : "))

    mn = int(input("Please Enter the minimum range : "))
    mx = int(input("Please Enter the maximum range : "))  

    if mn == mx:
        raise Exception(f"This not a range and mn is equal to mx")
    
    if mn>mx :
        raise Exception(f"Minimum number should not be greater than Maximum number : ")

    else:
            
        for i in range(mn,mx+1):
            if n % i == 0 :
                print(f"{i} is a divsior of {n} ")

            else:
                print(f"{i} is not a divisor of {n}")    

except Exception as e:
    print("Only integer is allowed")
    # raise ValueError(f"some error is occured")