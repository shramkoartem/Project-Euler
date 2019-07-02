import itertools
p = itertools.permutations([1,2,3,4,5,6,7])
opt = []
for i in p:
    i = list(i)
    opt.append(i)
opt = [[str(j) for j in i] for i in opt]
opt = [int(''.join(i)) for i in opt]
o = [i for i in opt if is_prime(i)]
o.sort(reverse=True)[0]
