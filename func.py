#Counts the occurrences or characters in a word

def sentence(statement):

    statement = " ".join(statement.split())

    print statement
    
    wordcount={}
    
    for word in statement.split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
             wordcount[word] += 1
    for key,value in wordcount.items():
         print key + " :", value


sentence("car : carpet as java : javascript!!&@$%^&")



