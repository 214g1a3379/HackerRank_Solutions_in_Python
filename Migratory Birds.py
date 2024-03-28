def migratoryBirds(arr):
    # Write your code here
    fr={}
    for i in arr:
        if i in fr:
            fr[i]+=1
        else:
            fr[i]=1
    l=max(fr.values())
    l1=[]
    for i in fr.keys():
        
        if fr[i]==l:
            l1.append(i)
    return min(l1)
