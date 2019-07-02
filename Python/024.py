
import itertools

a = '0123456789'
k = 10
res = []
for p in itertools.permutations(a, k):
    res.append("".join(p))

res[999999]
