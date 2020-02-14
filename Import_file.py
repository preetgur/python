import sys
print(sys.path)

import numpy as k
print("Version of numpy :",k.__version__)

print(f" This is the {__name__} file")


# from  python file basic.py
import import_file2     # recommended
print(import_file2.a)


import_file2.print_name("Gurpreet Singh")
# print_name(f"This is the {__name__} file ")


from import_file2 import a
print(a)