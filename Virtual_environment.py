# virtual environment is used to keep your application work correctly even when the new packages are available

# Because  Package is updated along with the time 

# suppose i am using version flask 1.0 and then the update of flask is available 
# when you use Pip install flask : then new version of flask is installed

# in new version some new function is availble or modified or deleted 
# in order to prevent this error we use virtual environment

print("Virtual environment is used to use same version of even the new version is available")

print(" #### All modules are installed separately in virtul environment ####")

print(" ####### pip install virtualenv ")
print(" #####how to install exact module : pip install ppandas==0.25.3")
print(" ####### pip uninstall pandas")

print("######## create virtual environment : virtualenv Environment_name")

print("Activate virtual environment : 1. By clicking on the activate folder")
print("######## using cmd : .\virtual_fodername\scripts\activate\n    example : .\preet_virtual\scripts\activate ")

print("#### create a virtual environment that as all the module as the python has : ")

print(" ##### use : virtualenv --system-site-packages virtual_environment_foldername ####")


print("Decativate : cmd deactivate")

print( " If error comes open : window powershell : write cmd : set-executionpolicy remotesigned")

print(" #### All modules are installed separately in virtul environment ####")

print("##### Create a requirement.txt file :  pip freeze > requirements.txt : It holds the details of module and its version")

print("Move the requirments.txt (send by someone) file just outside the virtual environment folder  and type below cmd : ")
print("#### Install all the module using requiremt.txt file : pip install -r .\requirements.txt")