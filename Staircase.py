def staircase(n):
    # Write your code here
    for i in range(n-1,-1,-1):
        for k in range(i):
            print(end=' ')
            
        for j in range(i,n):
            print('#',end='')
        print()
