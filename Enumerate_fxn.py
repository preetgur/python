li =["Bhindi","Aloo","Magi","Smosa","Tiki"]

i= 1
for item in li:
    if  i % 2 is not 0 :
        print(f" jarvis please by {item}")
    i +=1    


print("### Above code using enumerat fxn :")

print("Enumerate fxn has index and value already :")

# index =1
for index, item in enumerate(li):
    if index%2 == 0:
        print(f" jarvis please buy {item}")