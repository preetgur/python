# count the no of word in txt file

with open("Preet.txt") as f :
    a =0

    # print(f.read())  f.read()  works same the for loop does
    for i in f:     
        # print(i,end="")

        tokens = i.split(' ')   # return list
        print(tokens)
        print("lenght of token : ",len(tokens))  
        a += len(tokens)
        # write line and no of words
        # f.write(i+" word count"+str(len(tokens)))

    print("Total Words Counts : ",a) 
    
print(f.closed)        
