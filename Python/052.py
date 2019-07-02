def digits(n):
    digs = list(str(n))
    ans = [int(i) for i in digs]
    ans.sort()
    ans = [str(i) for i in ans]
    ans = int(''.join(ans))
    return ans
    
    
res = []
for i in range(100000, 1000000):
    ans = []
    for x in range(1,7):
        if digits(i*x) == digits(i):
            ans.append(True)
        else: 
            ans.append(False)
    if all(ans):
        res.append(i)
        
min(res)
