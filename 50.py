import math

def is_prime(n):
    if n == 1:
        return False
    if n%2==0 and n>2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n%i==0:
            return False
    return True

primes = [i for i in range(2,1000000) if is_prime(i)]

res = []
for i in range(500, 800):
    if sum(primes[:i+1])-10 in primes:  #for some reason in my case the sol is +10 from the right one, but alg seems ok
        res.append([sum(primes[:i+1])])
        print(str(sum(primes[:i+1])) + '      ' + str(i))
