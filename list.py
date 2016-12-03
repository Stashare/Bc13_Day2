"""MaxMin application"""
def minMax(numbersList):

    outputlist=[]#empty list to store max and min values

    temp_max=max(numbersList)
    temp_min=min(numbersList)

    if temp_max is temp_min: #if max and min values are equal,store one of them in outputlist.
       outputlist.append(temp_max)
       print "all numbers equal:",   sorted(outputlist)

    else: #store of max and min values in outputlist if they are not equal.
         outputlist.append(temp_min)
         outputlist.append(temp_max)
         print "minimum & maximum numbers respectively:",   sorted(outputlist)


minMax([4,4,4,4])


