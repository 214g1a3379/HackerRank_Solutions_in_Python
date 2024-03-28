def plusMinus(arr):
    # Write your code here
    p,n,z=[],[],[]
    for i in range(len(arr)):
        if arr[i]>0:
            p.append(arr[i])
        elif arr[i]<0:
            n.append(arr[i])
        else:
            z.append(arr[i])
    n1=len(arr)
    l=[len(p)/n1,len(n)/n1,len(z)/n1]
    print(l[0])
    print(l[1])
    print(l[2])
