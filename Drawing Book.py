def pageCount(n, p):
    # Write your code here
    
    c,c1=0,0
    for i in range(1,n+1):
        if i==p:
            break
        elif i%2!=0:
            c+=1
    for j in range(n,0,-1):
        if j==p:
            break
        elif j%2==0:
            c1+=1
    return min(c,c1)
