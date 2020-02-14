
# f= open("preet.txt")
# print(f.readline())
# f.close()

# we can use Block to open a file as :

with open("preet.txt") as f:
    print(f.readline(4))    # specify the range to show the characters

f= open("preet.txt")
print(f.readline())
f.close()
