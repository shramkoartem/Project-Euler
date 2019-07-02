import math

def comb(n, r):
    res = int(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))
    return res
    
ans = []
count = 0
for n in range(23,101):
    for r in range(1,n+1):
        if comb(n,r)>1000000:
            ans.append(comb(n,r))
            count += 1
            print(count)
