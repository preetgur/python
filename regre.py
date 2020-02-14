data = """
    Name : Gurpreet Singh
    Class : BTech Cse
    email : mr.gurpreetsingh936@gmail.com
    preetgur0137@gmail.com
    prtcbus@gmail.com
    sgursewaksingh11@gmail.com
    baljeetsinghSarpanch@gmail.com


     """
import re


# result = re.findall(r'\w+@\S+\w',data)
result = re.findall(r'[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+',data)

print(result)