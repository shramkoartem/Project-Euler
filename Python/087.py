def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n != 2:
        return False
    for d in range(3, int(n**0.5) + 1, 2):
        if n%d == 0:
            return False
    return True
    
def ppt(LIMIT, n_primes = 5000):
    primes = [n for n in range(2,n_primes) if is_prime(n)]
    ans = []
    
    for a in primes:
        if a**2 > LIMIT:
            break
        for b in primes:
            if a**2 + b**3 > LIMIT:
                break
            for c in primes:
                if a**2 + b**3 + c**4 < LIMIT:
                    ans.append(a**2 + b**3 + c**4)
                    
    return list(set(ans))
    
%%time
a = ppt(50000000, 10000)

# Wall time: 1min 52s
