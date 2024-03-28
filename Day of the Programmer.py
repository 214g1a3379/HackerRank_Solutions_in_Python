def dayOfProgrammer(year):
    # Write your code here
    if year<1918 and year>=1700:
        if year%4==0:
            s="12"+'.' +'09'+'.' +str(year)
            return s
        else:
            s="13"+'.' +'09'+'.' +str(year)
            return s 
    else:
        if year==1918:
            return '26.09.1918'
        else:
            if year%400==0 or (year%4==0 and year%100!=0):
                s="12"+'.' +'09'+'.' +str(year)
                return s
            else:
                s="13"+'.' +'09'+'.' +str(year)
                return s
