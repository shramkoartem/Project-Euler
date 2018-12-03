1001*1001
1002001

n = [i for i in range(1,1002002)]

res = []
count=0
step = 0
while len(res)<1002001:
    pos = 0
    try:
        for j in range(2,20000,2):
            for i in range(1,5):
                #step += j
                res.append(n[pos+step]) 
                step += j
            pos = res[-1]-1
            step = j
            count += 1
    except IndexError:
        break
        
sum(res)
