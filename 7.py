primes = []
n = 1000000
for p in range(2, n+1):
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        primes.append(p)
print('Done')

104743

bad!
