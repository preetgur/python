# pickle module
""" 
The pickle module implements a fundamental, but powerful algorithm for serializing and de-serializing a Python object structure. “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” 1 or “flattening”, however, to avoid confusion, the terms used here are “pickling” and “unpickling”. """

"""  
Any object in python can be pickled so that it can be saved on disk.

 Pickling is a way to convert a python object (list, dict, etc.) into a character stream. The idea is that this character stream contains all the information necessary to reconstruct the object in another python script.
"""
import pickle

# Pickling a python object

# car = ["Audi","BMW","Maruti Suzuki"]
# file = "mycar.pkl"

# fileobj = open(file,'wb')
# pickle.dump(car,fileobj)
# fileobj.close()


# Depickling

file ="mycar.pkl"
file_obj = open(file,'rb')
mycar = pickle.load(file_obj)
print(type(mycar)," : ",mycar)


""" 
 But there are other use cases as well which i found on stackoverflow. Let me list them below.

1) saving a program's state data to disk so that it can carry on where it left off when restarted (persistence)

2) sending python data over a TCP connection in a multi-core or distributed system (marshalling)

3) storing python objects in a database

4) converting an arbitrary python object to a string so that it can be used as a dictionary key (e.g. for caching & memoization).
 """