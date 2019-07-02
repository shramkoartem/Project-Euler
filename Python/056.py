def digsum(n):
    d = list(str(n))
    d = [int(i) for i in d]
    return sum(d)

m = 0
for a in range(1,100):
    for b in range(1,100):
        s = digsum(a**b)
        if s > m:
            m = s
m
