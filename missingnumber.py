"""MissingNumber"""

def find_missing(a,b):

    temparr=[]
    outputarr=[0]
    
    for i in b:
        if i not in a:
            temparr.append(i)
            outputarr=temparr
        
    print outputarr

find_missing([], [])





  	 


    