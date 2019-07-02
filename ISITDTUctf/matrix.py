
r="wsssddddaddsssssdddssdddwsdsdsdsdsssssddsdddssaadsddsddssddsddddsdsssdssdsdssdsdsdwsssdsdddsddddwsddddsdswsssdsdsddsssddsswwdssdssdddswddddsdwddswsasdssdddsdwdddsssddsddwsssdssdddswddsdsssdwwsdssdddawsdddsdwdsdsssssssddsddsdw"
d=[]
for i in range(15) :
    d.append([])

def readby3(s) :
    p=0
    for j in range(5) :
        for i in range(15) :
            for k in range(3) :
                d[i].append(s[p])
                p=p+1
    return d

def diagread(d) :
    s1=""
    s2=""
    for k in range(15) :
        s=""
        for i,j in zip(range(0,k+1,1),range(14-k,15,1)) :
            s1+=d[i][j]
            s+=d[j][i]
        s2=s+s2
    return s1+s2[15:]
    

def spiral(d) :
    s=""
    r=14
    c=0
    for i in range(8) :
        for i in range(r,c-1,-1) :
            s+=d[i][r]
        s=s[:-1]
        for i in range(r,c-1,-1) :
            s+=d[c][i]
        s=s[:-1]
        for i in range(c,r+1,1) :
            s+=d[i][c]
        s=s[:-1]
        for i in range(c,r,1) :
            s+=d[r][i]
        r=r-1
        c=c+1

    return s+ d[7][7]

def altread(s) :
    i=0
    j=1
    d=[]
    for i in range(15) :
        d.append([])
    p=0
    ns=""
    for i in range(0,15,2) :
        for j in range(15) :
            d[i].append(s[p])
            p=p+1
    for i in range(1,15,2) :
        for j in range(15) :
            d[i].append(s[p])
            p=p+1
    return d

def readfrom(d) :
    s=""
    for i in range(15) :
        if i%2==0 :
            for j in range(0,15) :
                s+=d[i][j]
        else :
            for j in range(14,-1,-1) :
                s+=d[i][j]
    return s

def findorgmatr(s) :
    s=s[::-1]
    p=0
    d=[]
    for i in range(15) :
        d.append([])
    for i in range(15) :
        for j in range(15) :
            d[j].append(s[p])
            p=p+1
    return d

if __name__ == "__main__" :
    #s=raw_input("Enter the string")
    print readfrom(findorgmatr(spiral(altread(diagread(readby3(r))))))




