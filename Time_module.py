
import time

initial = time.time()

print(initial)
for i in range(45):
    print("This is Garry")

print(f"for loop ran in : {time.time() - initial}")

initial2 = time.time()
k=0
while(k<45):
    print("This is Garry") 
    k +=1   

print(f"while loop ran in : {time.time() - initial2}")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

time.sleep(5)    # run after 5 seconds
print("Sleep sleep")