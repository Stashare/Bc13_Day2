"""Counts the occurrences or characters in a word"""

def sentence(statement):

    statement = " ".join(statement.split())#to get rid of \t,\n and whitespaces

    
    wordcount={}
    #a loop for counting all words in the statement
    for word in statement:
        if word not in wordcount:
            wordcount[word] = 1
        else:
             wordcount[word] += 1
    for key,value in wordcount.items():
         print key + " :", value


sentence("car : carpet as java : javascript!!&@$%^&")



