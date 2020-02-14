# comprehension

ls = []
for i in range(100):
    if i%3 == 0:
        ls.append(i)

# print(ls)

# same as above in one linear : list comprehension

ls2 = [i for i in range(100) if i%3 == 0]
print(ls2)

# Dictionary - comprehension
# ex : dict1 = {0 : "item0", 1:"item1", 2:"item2"}

dict1 = {f"key{i}":f"value{i}" for i in range(1,10) if i%2 == 0}
print("########## Dict ########")
print(dict1)

# reverse key-value pair
dict2 = {f"key{i}":f"value{i}" for i in range(1,10)}
dict2 = {value:key for key,value in dict2.items()}

print("#### Reverse Dictionary #####\n ",dict2)

# set - comprehension : remove duplicate value
print("#####  Set-Comprehension #####")
dress = { dress for dress in ["dress1","dress1","dress2","dress2"]}
print(type(dress),dress)


# generator - comprehension
evens = (i for i in range(100) if i%2==0)
print(evens)
print(evens.__next__())
print(evens.__next__())

print("## before")
for i in evens:
    print(i)

