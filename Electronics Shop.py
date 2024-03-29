def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    l=[]
    for i in keyboards:
        for j in drives:
            if i+j<=b:
                l.append(i+j)
    if len(l)==0:
        return -1
    else:
        return max(l)
