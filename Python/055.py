def pol(n):
    d = list(str(n))
    for i in range(0,len(d)):
        if d[i] != d[-(i+1)]:
            return False
    return True

def reverse(n):
    d = list(str(n))
    d = d[::-1]
    d = int(''.join(d))
    return d

def lychrel(x):
    for j in range(0,50):
        rx = reverse(x)
        y = x+rx
        if pol(y):
            return True
        else: x = y    
        if j == 49 and not pol(y):
            return  False
            
            
res = []
for x in range(0,10000):
    if not lychrel(x):
        res.append(x)
        
len(set(res))
