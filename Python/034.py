import math

res = []

for i in range(100000):
    digits = [int(j) for j in list(str(i))]
    s = sum(math.factorial(d) for d in digits)
    if s==i:
        res.append(i)
        print(i)
