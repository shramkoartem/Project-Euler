res = []
for a in range(1,1000):
    for b in range(1,1000):
        if a**2+b**2-(1000-a-b)**2 == 0:
            c = 1000 - a - b
            res.append([a,b, c])
            print(a,b)

res 
[[200, 375, 425], [375, 200, 425]]
res = res[0]
res[0]**2 + res[1]**2-res[2]**2
0
res[0]*res[1]*res[2]
31875000
