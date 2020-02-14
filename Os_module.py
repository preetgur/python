# Excersice to change the name of file using os

import os

# print(dir(os))
print("Current working Directory : ",os.getcwd())
os.chdir("c:/Users/Gurpreet/Desktop")
print(os.getcwd())
# print(os.listdir("C:/Users/Gurpreet/Desktop"))  # create the list of all present on desktop

desktop = os.listdir("C:/Users/Gurpreet/Desktop")

for i in desktop:
    print(i)

# os.mkdir("new folder using os2") # create new folder in current working directorye

# os.makedirs("Game/PUBG")  # create folder and sub folder

# os.rename("Game","PuBG game")
# print(os.environ.get("Path"))
print(os.path.join("c:/Users/Gurpreet/Desktop","practice.txt"))
print(os.getcwd())

print(os.path.exists("c:/Users/Gurpreet/desktop/practice.txt"))

print(os.path.isdir("c:/Users/Gurpreet/Desktop/PuBG game"))
print(os.path.isfile("c:/Users/Gurpreet/Desktop/practice.txt"))