""" 
        File Basic

"r" - open file for reading  [ defalut]
"w" - open file for writing
"x" - create file if not exits
"a" - Add more content to a file
"t" - text mode  [ Default ]
"b" - binary mode
"+" - read and write mode

 """

print("####### One Way to Access file : f.read() ##########")

f = open("preet.txt","rt")   # f is file pointer or called file handler

content = f.read()
print(content)

f.close()


print("####### Second Way to Access file  : for loop ##########")

#imp: use for loop to read the file not [f.read()]

f1 = open("preet.txt","rt")

for i in f1:
        print(i,end="")
f1.close()

print("\n####### Third Way to Access file : f.readline() ##########")


f2 = open("preet.txt","rt")

print(f2.readline(),end="")                  # print first line
print(f2.readline(),end="")                  # print second line

f2.close()

print("\n####### Store the all lines in a List using : f.readlines() ##########")


f3 = open("preet.txt","rt")

print(f3.readlines(),end="")                  # print first line

f3.close()


print("\n####### How to write in a file 'w' : f.write() ##########")


f4 = open("preet.txt","w")

f4.write("First Line")

f4.close()


print("\n####### How to write in a file using append 'a' : f.write() ##########")


f5 = open("preet2.txt","a")

f5.write("Second Line\n")

f5.close()

print("\n####### How to calculate no of character  write : a = f.write() ##########")


f6 = open("preet2.txt","a")

no_of_characters = f6.write("Second Line can you ges\n")

print("No of Characters currently written : ",no_of_characters)
f6.close()


print("\n####### Read and Write Both : ##########")


f6 = open("preet2.txt","r+")
print(f6.read())
print("#### After Writing into file ")
f6.write(" *******Third Line\n")
print(f6.read())

f6.close()


print("\n####### More to Files : ##########")



f7 = open("preet2.txt")
# print(f7.read())
print(f7.readline())
f7.seek(11)              # It tells from where to start reading the file

print(f7.tell())                 # tells where the file handler pointer (f7)
print(f7.readline())
# print(f7.tell())
print(f7.readline())

f7.seek(0)              # It tells from where to start reading the file
print(f7.readline())

f7.close()

