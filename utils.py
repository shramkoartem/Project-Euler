def prime(n):
    if n == 2:
        return True
    
    if n%2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n%i == 0:
            return False
    return True
    
    
primes = [i for i in range(1,100001) if prime(i)]

def digits(n):
    ans = str(n)
    ans = int("".join(sorted(ans)))
    return ans
