from itertools import compress

def rwh_primes1v1(n):
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

primes = rwh_primes1v1(10000)

def digits(n):
    d = list(str(n))
    d.sort()
    return int(''.join(d))

pr = [i for i in primes if len(list(str(i)))==4]

for i in range(0,len(pr)):
    for j in range(1,int(len(pr)/2)):
        a = pr[i]
        b = pr[i+j]
        if digits(a) == digits(b):
            dif = b-a
            c = b+dif
            if c in pr:
                if digits(a)==digits(c):
                    print(a, b, c)
