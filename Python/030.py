
def digsum(num):
    a = list(str(num))
    s = sum([int(i)**5 for i in a])
    if num == s:
        ans = num
    else:
        ans = 0
    return ans
 
res = []
for i in range(1000,1000000):
    res.append(digsum(i))

sum(res)

443839

for i in res:
    if i!=0:
        print(i)
