def getTotalX(a, b):
    # Write your code here
    c=0
    for i in range(1,101):
        if all(i%num==0 for num in a):
            if all(num%i==0 for num in b):
                c+=1
    return c
