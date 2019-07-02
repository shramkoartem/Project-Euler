import itertools

digits = [i for i in range(1,10)]
a = itertools.permutations(digits, 9)

combs = []
for i in list(a):
    combs.append(i)

len(combs)
362880

products = []

for i in range(1,5):
    for t in combs:
        a = t[:i]
        b = t[i:5]
        c = t[5:]
        a = int("".join(str(i) for i in list(a)))
        b = int("".join(str(i) for i in list(b)))
        c = int("".join(str(i) for i in list(c)))
        if a*b == c:
            if c not in products:
                products.append(c)

sum(products)
