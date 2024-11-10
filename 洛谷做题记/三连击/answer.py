a=123
array=['1','2','3','4','5','6','7','8','9']

while a<333:
    a+=1
    b=2*a
    c=3*a
    a1=str(a)
    b1=str(b)
    c1=str(c)
    array2=[]
    for i in range(3):
        if a1[i] not in array2:
            array2.append(a1[i])
        if b1[i] not in array2:
            array2.append(b1[i])
        if c1[i] not in array2:
            array2.append(c1[i])
        array2.sort()
        if array2==array:
            print(a,b,c)
            
