

def matching_Word(sentence1,sentence2):
    print("######### Stirng : ",sentence2) # string
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")  # list
    print("######## List : ",words2)
    score = 0
    for i in words1:        # convert list into string
        for j in words2:
            # print(type(i))   :string
            
            print(f"Matching {i} with {j}")
            if i.lower() == j.lower():
                score +=1
    return score            

if __name__ == "__main__":
    # print(matching_Word("This is Python","Python is good"))
    sentences = ["python is a good","this is a snake","harry is a good boy","Subscribe to code"]

    query = input("Please enter the query string\n")
    scores = [matching_Word(query,sent) for sent in sentences ]    # send the string one by one to matching fxn 
    # convert the sentences [list ]  into sent [str]
    print(f"{type(scores)} and {scores}")   # list

# sentences and scores both are list :
    print(f"{sentences} and {scores}")      
    sorted_Sent_Scor = [ sentScore for sentScore in sorted(zip(scores,sentences),reverse=True) if sentScore[0] != 0]
    print(sorted_Sent_Scor)
    print(type(sorted_Sent_Scor))    # list

    print(f"{len(sorted_Sent_Scor)} result found ! ")
###########f # many values to unpack : that's why use score,itme to unpack :[(1,"Python is good")]
    for score,item in sorted_Sent_Scor:   
        print(f" \"{item}\" : with a score of {score}   ")


    li = [("hi",45),(78,45),(43,"ab"),("aslkjf",00)]

    for i,j in li:
        print(f" {i} and {j}")    