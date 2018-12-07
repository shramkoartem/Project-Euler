def digs(n):
    d = list(str(n))
    return len(d)
    
res = []
count = 0
for i in range(1, 100):
    for p in range(1,100):
        if digs(i**p) == p:
            count += 1
            res.append(i**p)
            print(str(i)+'^'+str(p)+' = '+str(i**p))
            
 len(set(res))
 
