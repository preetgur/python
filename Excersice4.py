#Project change the name of file
import os

def soldier(dir_path,file_name,extension):

    # print("Current Working Directory : ",os.getcwd())
    os.chdir(dir_path)
    # print("New Working Directory : ",os.getcwd())
    i = 1 
    file_in_chdir = os.listdir(dir_path)             # create the list of all files in user directory
    # print(file_in_chdir)

    
    with open(file_name) as f:
        print(f.readlines())   
        file_list = f.read().split("\n") 
        print(file_list)                               # prints ['']

    for allfiles in file_in_chdir:
        print(allfiles)  # print all files 

        #captilize the file name
        if allfiles not in file_list:  
            os.rename(allfiles,allfiles.capitalize())

        #change the name of file start from 1 : based on extension
        if os.path.splitext(allfiles)[1] == extension:
            os.rename(allfiles,f"{i}{extension}")
            i +=1    




if __name__ == "__main__":

    dir_path_name = input("Please Enter the Path of Directory")
    file_name = input("Please Enter the name of file which has the prohibited words : ")
    ext = input("Please Enter the name of Extension")
    soldier(dir_path_name,file_name,ext)
    