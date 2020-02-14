"""
Iterable - __iter__()  or __getitem__()
Iterator - __next__()
Iteration - 
"""

# generator : runs only one time

def gen(n):
    for i in range(n):
        yield i

g = gen(3)
print(g.__next__())   
print(g.__next__())        
print(g.__next__())        
# print(g.__next__())    # gives error because value exceeds

for i in g:    # it does not show output because we run second time
    print(i) 


# Ex : of iterable

h = "harry"

for i in h:
    print(i)

# or
print("########## Second way")
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

