a = "hello"

def print_name(x):
    print(f"Your name is : {x}")


def main_fxn(string):
    print(f"This fxn is inside the __main__ : {string}")

# important : when we will import this file then we will able to use above written fxn using (.) as shown below:
# import import_file2     
# print(import_file2.a)

# but the code written inside the main would'nt be useabel outside this file

# print(f"This is the {__name__} file ")
# print_name(f"This is the {__name__} file ")


if __name__ == "__main__" :

    main_fxn("Gurpreet Singh")

    print_name("outside the name")


# You can check whether the ( fxn or the file )is from imported file or from the main file using 


print(f"This is the {__name__} file ")
print_name(f"This is the {__name__} file ")