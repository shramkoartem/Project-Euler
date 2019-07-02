triangular = [int(0.5*n*(n+1)) for n in range(1,100000)]
hexog = [n*(2*n-1) for n in range(1,100000)]
pent = [int(n*(3*n-1)/2) for n in range(1,100000)]

for n in triangular:
    if n in hexog and n in pent:
        print(n)
