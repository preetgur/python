# practice problem : Food and Calories

print("Enter the numbers of the list one by one \n")
size = int(input("Enter size of list : "))
mylist = []

for i in range(size):
    mylist.append(int(input(f"Enter {i+1} items : ")))

print(f"Your list is {mylist}")

#Storing the list in another varible 
# reverse1 = mylist #if we don't use [:] then our original list is also reversed
reverse1 = mylist[:]    # copy the list
reverse1.reverse()
print(f"My First Reversed list : {reverse1} and orignial : {mylist}")

print(f"Second way to Reverse the list using list slice : {mylist[::-1]}")
reverse2 = mylist[:]  
for i in range(len(reverse2)//2):
    print(f"#### After :Length of reverse2 list: '{len(reverse2)} ': and reverse [i] : 'at index : {i} = {reverse2[i]} ' and reveres[len(reverese)-i-1] : reverse2[{len(reverse2) -1 -i}] ='{reverse2[len(reverse2)-i -1]}' ")


    reverse2[i], reverse2[len(reverse2)-i -1] = reverse2[len(reverse2)-i -1],reverse2[i]
    
    print(f"=>>>>>>>>> The reversed list at i = {i} is {reverse2}")
    print(f"#### After :Length of reverse2 list: '{len(reverse2)} ': and reverse [i] : 'at index : {i} = {reverse2[i]} ' and reveres[len(reverese)-i-1] : reverse2[{len(reverse2) -1 -i}] ='{reverse2[len(reverse2)-i -1]}' ")


print(reverse2)
print(f"Third reversed list of {mylist} is {reverse2}")


