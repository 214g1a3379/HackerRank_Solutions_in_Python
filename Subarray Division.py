def birthday(s, d, m):
    # Write your code here
    c=0
    for i in range(len(s)-m+1):
        sa=s[i:i+m]
        if sum(sa)==d:
            c+=1
    return c
    
