import itertools

p = itertools.permutations([1,2,3,4,5,6,7,8,9])

opt = []
for i in p:
    i = list(i)
    opt.append(i)
opt = [[str(j) for j in i] for i in opt]
opt = [int(''.join(i)) for i in opt]
opt = [str(i) for i in opt]
res = []
for i in range(10000, 8000, -1):
    num = ''
    for j in range(1,10):
        num += str(i*j)
        if num in opt:
            res.append(int(num))
            print(num)
            
max(res)
