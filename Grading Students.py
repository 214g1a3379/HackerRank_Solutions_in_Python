def gradingStudents(grades):
    # Write your code here
    l=[]
    for i in grades:
        if i<=35:
            
            l.append(i)
        else:
            if i%5==3:
                l.append(i+2)
            elif i%5==4:
                l.append(i+1)
            else:
                l.append(i)
    return l
