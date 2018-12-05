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
    
def digits(n):
    digs = list(str(n))
    ans = [int(i) for i in digs]
    ans.sort()
    ans = [str(i) for i in ans]
    ans = int(''.join(ans))
    return ans

def rotate(n,i):
    digs = list(str(n))
    ans = digs[i:] + digs[:i]
    return int(''.join(ans))

primes = [i for i in range(2,1000000) if is_prime(i)]
cp = []
count = 0
for n in primes:
    if n not in cp:
        ans = []
        for i in range(0, len(str(n))):
            ans.append(is_prime(rotate(n,i)))
        if all(ans):
            count +=1
            cp.append(digits(n))
            print(count)
