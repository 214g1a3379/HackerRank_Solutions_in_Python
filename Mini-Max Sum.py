def miniMaxSum(arr):
    # Write your code here
    l=[]
    s=sum(arr)
    for i in range(len(arr)):
        l.append(s-arr[i])
    print(min(l),end=' ')
    print(max(l),end='')
        
