import math
from operator import itemgetter

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
 
 #b can only be a positive prime -> reduce the feature space
 b_primes = [i for i in range(0,1001) if is_prime(i)]
 
    
 def n_primes(a,b):
    n=0
    num = n**2+a*n+b
    
    while is_prime(num):
        num = n**2+a*n+b
        if num<0:
            break    
        n += 1
    return n-1
    
 res = [[n_primes(a,b),a*b] for a in range(-1000,1000) for b in b_primes] 
 x = sorted(res, key=itemgetter(0), reverse=True)
 x[:10]
