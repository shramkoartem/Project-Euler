cubes = [i**3 for i in range(5000,10000)]

def digits(n):
    ans = str(n)
    ans = int("".join(sorted(ans)))
    return ans
    
n = [[i,digits(i)] for i in cubes]

k = [i[1] for i in n]

m = list(set(k))

res = []
for j in m:
    a = []
    c = 0
    for h in n:
        
        if j == h[1]:
            c += 1
            a.append(h[0])
    res.append([a,c])
    
for i in res:
    if i[1] == 5:
        print(i[0][0])
