import itertools
def per(i): 
    l = itertools.permutations(str(i))
    return [int(''.join(x)) for x in l]
p = per(1023456789)

from itertools import compress

def rwh_primes1v1(n):
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

primes = rwh_primes1v1(100)

def check(n):
    digs = list(str(n))
    
    ans = []
    for i in range(0,7):
        if int(''.join(digs[i+1:i+4])) % primes[i] == 0:
            ans.append(True)
        else:
            ans.append(False)
    return all(ans)
    
res = sum([i for i in p if check(i)])
