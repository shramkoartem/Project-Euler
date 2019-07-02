def is_prime(n):
    if n == 1:
        return False
    
    if n == 2:
        return True
    
    if n%2 == 0:
        return False
    
    for i in range(3, int(n**0.5)+1,2):
        if n%i == 0:
            return False
    return True

def prime_facts(n):
    d = [i for i in range(2,round(n/2)+1) if n%i==0 and is_prime(i)]
    return d

primes = [i for i in range(2,1000000) if is_prime(i)]

n = 1
i = 0
for i in range(0,10): 
    n = n*primes[i]
    print(n)
    
    
f = prime_facts(510510)
fn = 510510
for d in f:
    fn = fn*(1-1/d)
nfn = i/fn


