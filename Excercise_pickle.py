# import pickle

# file ="iris.txt"
# file_obj = open(file,'r')
# mycar = pickle.load(file_obj)
# print(type(mycar)," : ",mycar)

import requests

url =  "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

iris = requests.get(url).text
iris_list = iris.split('\n')
# print(iris.status_code)
print("######################",iris_list)
# print(iris_list)
iris_li = [i.split(",") for i in iris_list if len(i)!= 0]
print("########################",iris_li)

print(type(iris),type(iris_list),type(iris_li))

# print(str(iris).split(","))

# ir = list(iris)

# print(ir.__dir__())
# print(ir.split(" ,"))
# for i in ir:
#     print(i.split(" "))

# file_obj = open(file,'rb')
# mycar = pickle.load(file_obj)
# print(type(mycar)," : ",mycar)
