def birthdayCakeCandles(candles):
    # Write your code here
    d={}
    for i in candles:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return max(d.values())
