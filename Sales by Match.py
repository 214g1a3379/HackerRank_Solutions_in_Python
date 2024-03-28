def sockMerchant(n, ar):
    # Write your code here
    fr={}
    for i in ar:
        if i in fr:
            fr[i]+=1
        else:
            fr[i]=1
    l=list(fr.values())
    c=0
    for i in l:c+=i//2
    return c
