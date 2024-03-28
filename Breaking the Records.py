def breakingRecords(scores):
    # Write your code here
    maxi=scores[0]
    mini=scores[0]
    c,c1=0,0
    for i in scores:
        if i>maxi:
            maxi=i
            c+=1
        if i<mini:
            mini=i
            c1+=1
    return c,c1
