from itertools import compress

def rwh_primes1v1(n):
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

primes = rwh_primes1v1(10000)

def is_gold(n):
    for p in primes:
        if p < n:
            for i in range(1,200):
                if p+2*i**2 == n:
                    return True
    return False
    
n = 9
ans = True
while ans:
    n += 2
    if n not in primes:
        ans = is_gold(n)
    else:
        ans = True
n
