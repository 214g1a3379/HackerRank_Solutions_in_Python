def divisibleSumPairs(n, k, ar):
    # Write your code here
    c=0
    for i in range(n):
        for j in range(i+1,n):
            if (ar[i]+ar[j])%k==0:
                c+=1
    return c
