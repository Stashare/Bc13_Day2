"""MissingNumber"""

def find_missing(a,b):

    temparr=[] #an array that stores missing numbers temporarily during the loop 
               #and it is assigned to outputarr.
    
    outputarr=[0] #output the final result
    
    #loop to check whether there is missing numbers
    for i in b:
        if i not in a:
            temparr.append(i)
            outputarr=temparr
        
    print outputarr

find_missing([], [])#A call to the find_missing function,passing arrays as parameters
                    #the output should be [0]





  	 


    