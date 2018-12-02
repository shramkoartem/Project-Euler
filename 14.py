res=1
dat = []
for i in range(999999,500000,-1):
    n = i
    C = [n]
    while n!=1:
        if n%2==0:
            n=n/2
            C.append(n)
        else:
            n=3*n+1
            C.append(n)
    if len(C)>res:
        res = len(C)
        dat.append([i,res])
print(dat)

[[999999, 259], [999667, 290], [999295, 396], [997823, 440], [970599, 458], [939497, 507], [837799, 525]]

ans 837799
