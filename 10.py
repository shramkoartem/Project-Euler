res = []
def primes(n):
    for i in range(2, n+1):
        for j in range(2, int(i/2)+1):
            if i%j == 0:
                break
        else:
            res.append(i)
primes(2000000)
sum(res)
