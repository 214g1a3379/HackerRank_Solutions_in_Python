def diagonalDifference(arr):
    # Write your code here
    s,s1=0,0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j :
                s+=arr[i][j]
            if i+j==n-1:
                s1+=arr[i][j]
    return abs(s-s1)
