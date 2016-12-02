def minMax(numbersList):

    outputlist=[]

    temp_max=max(numbersList)
    temp_min=min(numbersList)

    if temp_max is temp_min:
       outputlist.append(temp_max)
       print "all numbers equal:",   sorted(outputlist)

    else:
         outputlist.append(temp_min)
         outputlist.append(temp_max)
         print "minimum & maximum numbers respectively:",   sorted(outputlist)


minMax([4,4,4,4])


