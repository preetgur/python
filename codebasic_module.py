# module is a way to reuse a code   written by someone else

"""
# when file is present in current directory

import filename 

import filename as f 

# when file present in subdirectory/ sub folder

import foldername.file as f

# when file present somewhere else in system:
To find  a module, python will use current directory and then all directions listed in system path

import sys
sys.path.append("module path c:\code")

"""

print(1,2,3,sep='*')
print(3 >= 3) 