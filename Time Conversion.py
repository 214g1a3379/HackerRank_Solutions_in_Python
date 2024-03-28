def timeConversion(s):
    # Write your code here
    if s[-1]=='AM':
        return ((int(s)-12:00:00)'AM')
    else:
        return ((int(s)+12:00:00)'PM')
