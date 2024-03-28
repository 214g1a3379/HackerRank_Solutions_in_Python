def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    ap=0
    for i in apples:
        if a+i>=s and a+i<=t:
            ap+=1
    ora=0
    for j in oranges:
        if b+j>=s and b+j<=t:
            ora+=1
    print(ap)
    print(ora)
