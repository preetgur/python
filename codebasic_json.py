# Json
"""
JSON : Java Script object Notation
It is a data exhange format similar to xml
 """
# create address book and write some records into it
# Read this address book
"""
Proceduer : 
1. First create Dictionary {key:value} pair
2. import json and convert it into json data(string) format using "json.dumps(dict)" so that other language can use it.

#Reading json using Python 
3. import json and convert the string into json using " json.loads(json_string) "

 """

book = {}    #dict
# book[]
book["tom"] = {
    "name": "tom",
    "address" : "1 green street,NY",
    "Phone":991420
}

book["bob"] = {
    "name": "Bob",
    "address" : "1 red street,NY",
    "Phone":98141
}

print("#### Dictonary #####")
print(type(book)," : ",book)

import json
s = json.dumps(book,sort_keys=True,separators=(",",":"))  # convert the "dict" into string using 'dumps' and converted into json 

#now you can put in the file
print("#### Dict Into JSON #####")

print(type(s)," : ",s)
"""
You can now read this JSON data (s) using any language that supports JSON such as javascript, c++,etc.
Hence this is called data exhanging format (i.e exchanging data from python  program into javascript program )
"""

# write into file
with open("json_file.txt","w") as f:
    f.write(s)

# read file
print("######## Read File #######")
with open("json_file.txt") as f :
    f = f.read()
    print("### Read as a String ")
    print(type(f)," : ",f)
    # print(f['bob'])        # Not working because it is a string
    
    print("#### Read as Json")
    book = json.loads(f)
    print(type(book)," : ",book)
    print("Bob MObile : ",book['bob']['Phone'])       # works because convert into dict

    # Take input from user 
    user_input = input("Enter key name : ")

    # print(user_input in book)
    if user_input in book:
        print("User is Present")
        print("User Data : ",book[user_input])
    else:
        print("user is not present")    

    book["tom"].clear()
    print("Tom dictionary is Clear : ",book)    



""" 
List : all values have similar meaning

Tuple : all values have different meaning

Ex : list

expense_list = [2300,545,564654]

list_of_name = ["bob","tom","partha"]

Ex : tuple

point = (4,6)  # 4 is x cordinate , 6 is  y cordinate
address = ("1 purple street ", "newyork",1001)

"""
