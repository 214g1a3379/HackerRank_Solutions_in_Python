def compareTriplets(a, b):
    # Write your code here
    alice,bob=0,0
    for i in range(len(a)):
        if a[i]>b[i]:
            alice+=1
        elif a[i]<b[i]:
            bob+=1
    l=[alice,bob]
    return l
