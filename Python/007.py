# update 09.07.2019

def isprime(n):
    if n < 2:
        return False
    if n%2 == 0 and n != 2:
        return False
    
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

primes = [i for i in range(200000) if isprime(i)]

primes[10000]
#104743

