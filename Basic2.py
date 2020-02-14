print("Basic of Python ")
message = "gurpreet is a GOOD boy 97"

print(message.isalnum())

print(message.endswith("97"))
print(message.count("o",2,22))   # count(text,staringFrom,Toindex)

print(message.capitalize())
print(message.upper())
print(message.lower())
print(message.replace("97","1997"))
print(message.find("boy"))   # return -1 on failure


print("###########################  Lists [] #############################")

"""
 Mutable - Can change
 Immutable - cannot change

 """

""" List are mutable """

print("List in Python : ")

grocery = ['Harpic','vim bar','deodrant']
print(grocery)
print(grocery[2])

print("########## How to shuffle the List ############")

from random import shuffle
grocery2 = ['Harpic','vim bar','deodrant']
shuffle(grocery2)
print("Shuffle list :",grocery2)

numbers = [12,4,5,89]
print(numbers)

numbers.sort()
print("Sorting of list : ",numbers)

numbers.reverse()
print("Reverse of list : ",numbers)

print("slicing of list : ",numbers[1:3])

numbers.remove(5)        #Remove the value '5' from the list
grocery.remove("vim bar")
print("Removig the element 5 from list : ",numbers,"remove vim bar from grocery list : ",grocery)

############## create list of list

list_of_list =[numbers,grocery]
print("############### List of list :",list_of_list)

numbers.append(99)   # append at the end of list
numbers.append(9)
print(numbers)

numbers.insert(2,44)   # Add element by specifiying its index value and the value it self 
numbers.pop()   # remove element from the laste
numbers.pop(2)  # remove element with 'index'

del numbers[1 : 3]  # remove the elements of index bw 1 -3
print(numbers)

numbers.extend((45,5,8,7))   # Adding the new elements in the list
print(f"############ Extending the list : {numbers}")

numbers[1] = 100        # update 100 at index 1
print("update the value : ",numbers)

numbers = []
print("Empty list :",numbers, type(numbers))


""" Tuple are Immutable """
print("###########################  Tuple () ######################")
tup = (1,12,5,1,8,1)
print(tup,type(tup))
print(f"########### count : {tup.count(1)}")   # It counts the no of times occurens of some value

# tup.append(999)                 'tuple' object has no attribute 'append'
# tup.insert(2,66)                'tuple' object has no attribute 'insert'
# tup.remove(12)                  'tuple' object has no attribute 'remove'
# tup.pop()                       'tuple' object has no attribute 'pop'
# tup.sort()                      'tuple' object has no attribute 'sort
# tup.reverse()                   'tuple' object has no attribute 'reverse'
# tup[1] = 100                    'tuple' object does not support item assignment

print(tup)

tup2 =()
print(tup2 ,type(tup2))

tup3 =(5)              # string
print(tup3 ,type(tup3))

# You have to put , if you have only single element in the tuple if you don't put then it assume something else

tup4 =(5,)           # tuple : using ,
print(tup4 ,type(tup4))


print("###########################  Dictionary {} ######################")

d1 = {}  #empty dictionary
print(type(d1))

d2 = {
    "Name": "Gurpreet Singh",
      "Mobile No": 9914204589,
      "Address": "Village Khandoli",
      "Qualification":"Btech[CSE]",
      "First Year":{"sem1":"All Clear", "sem2":56},
      "Second Year": {"sem3": {"Subjects": {"Hindi":55,"Punjabi":50,"English":"all clear"}}},
      "list": [45,78,98,"This is list ","Do you know"]

      }

print(d2)      
print(d2["Mobile No"])
print(d2["First Year"]["sem1"])
print(d2["Second Year"]["sem3"]["Subjects"])
print(d2["Second Year"]["sem3"]["Subjects"]["Punjabi"])
print(d2["list"])

print(d2.get("ABC","Not Found key"))   # if key is not available then it show "Not found key"

d2["Mobile No"] = 6284192183
print("Mobile no updated :",d2["Mobile No"])

print(d2.get("Second Year"))

d2["Second Year"]["sem3"]["Subjects"]["Punjabi"] = 99    # punjabi marks updated
print("Punjabi Marks Updated :",d2["Second Year"]["sem3"]["Subjects"]["Punjabi"])

d2["New Field"] = "New folder Added"   # Added new Key

print("Key is Added :",d2["New Field"])
print("#################################################")
d2Copy = d2.copy()
print("Copy Of Dictionary : \n",d2Copy)

print("#################################################")

del d2Copy["Second Year"]
del d2Copy["First Year"]

print("Delete the Second Year and First Year key : \n",d2Copy)
print("#################################################")

print("This is the original Dictonary Not Affected : \n",d2)

print("#################################################")


d2["Mobile No"] = 9914204589   # Added new Key 
d2.update({"Mobile No" : 9814143615})
print(d2)

print("######################### Print All the keys########################")

print(d2.keys())
print(d2["Second Year"].keys())
print(d2["Second Year"]["sem3"]["Subjects"].keys())

print("######################### Print All the items ########################")

print(d2.items())
print(d2["Second Year"]["sem3"]["Subjects"].items())

# Taking input from user inside the list

username = input("Enter username : ")
d3 = {"Name":username}
print("Dict : ",d3)

d4 = {}
enterKey = input("Please Enter the name of key :")
enterValue = input("Please Enter the value : ")

d4[enterKey] = enterValue
print("key and value are :",d4)

#################################  Creating dictonary form two lists:

list1 = ["Name","Mobile_No","Address","Email_id"]
list2 = ["Gurpreet",9914204589,"village Khandoli","preetgur0137@gmail.com"]

dict_list = dict(zip(list1,list2))
print(f"######## Dict created from list : {dict_list}")
print(f"List all the  keys : {dict_list.keys()}")

print("######################### Set () ########################")
""" Set only have the singular value duplicate value are not allowed """
s = set()  # empty set

set_from_list = set([1,2,2,3,6,5,6])
print(set_from_list)

list1 = [ 1,"Gurpreet ",6]
set_from_list1 = set(list1)
print(type(set_from_list1),set_from_list1)

s.add(1)
s.add(1)
s.add(2)
s.add(9)
s.add(45)
print("Adding value in set :",s)

s.remove(45)
print("Remove the 45 :", s)

s.union({1,2,3})  # wrong we have to store it into a varibale 
print("Union :",s)

s1 =s.union((1,2,3))
print("Union second :",s1)

s1 =s.intersection((1,2,3))
print("Intersection :",s1)

s1 =s.isdisjoint((1,2,3))    # retrun boolean value
print("Disjoint :" ,s1)
