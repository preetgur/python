a = input("What is your name : ")
b = int(input("How much do you earn : "))

if b==0:
    raise ZeroDivisionError("B is 0 so stopping the program.")
if a.isnumeric():
    raise Exception("Numbers are not allowed")

print(f"Hello, {a}")


c = input("Enter your name : ")

try:
    print(l)

except Exception as e:
    if c =="harry":
        raise ValueError("Harry is blocked")

    print("Exception handled")