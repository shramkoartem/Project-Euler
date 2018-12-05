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

def check(n):
    digs = list(str(n))
    ans = []
    for i in range(1,len(digs)):
        left = int(''.join(digs[i:]))
        right = int(''.join(digs[:-i]))
        ans.append(is_prime(left))
        ans.append(is_prime(right))
    return all(ans)

res = []
for n in primes:
    if check(n):
        res.append(n)
        
len(res)
