n = [i for i in range(1,1002)]

res = []
step = 0
while len(res)<1001:
    pos = 0
    try:
        for j in range(2,100,2):
            for i in range(1,5):
                #step += j
                res.append(n[pos+step]) 
                step += j
            pos = res[-1]-1
            step = j
    except IndexError:
        break
res
