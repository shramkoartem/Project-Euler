import math

res=[]
for p in range(1000,800,-1):
    count = 0
    for a in range(20,int(p/2)):
        for b in range(20, int(p/2)):
            c = math.sqrt(a**2+b**2)
            if a+b+c == p:
                count += 1
    res.append([p,count])
    print(str(p)+'   '+str(count))
