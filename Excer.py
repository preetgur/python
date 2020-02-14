# os

import os

def soldier(path,file_path,extension):
    os.chdir(path)
    print(os.getcwd())
    list_file_in_chdir = os.listdir(path)
    

    with open(file_path) as f:
        f = f.readlines()   
        
        for i in f:
            print("file : ",i,end="")
 

    for j in list_file_in_chdir:
        print(j)

        if j not in i:
            os.rename(j,j.lower())
            print("lower case")

        else:
            print("not Excecuted :")    

        k = 1
        if os.path.splitext(j)[1] == extension:
            os.rename(j,f"{k}{extension}")
            k +=1    

if __name__ == "__main__":

    print("###############################")

    soldier("c:/Users/Gurpreet/Desktop/Pubg game","c:/Users/Gurpreet/Desktop/Python/Preet.txt","jpg")