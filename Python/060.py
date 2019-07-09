# slow

def isprime(n):
    if n < 2:
        return False
    if n%2 == 0 and n != 2:
        return False
    
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

def merge(a, b):
    return int(str(a)+str(b))

def check(a, b):
    return isprime(merge(a, b)) and isprime(merge(b,a))
    
primes = [i for i in range(10000) if isprime(i)]

res = []

for i in range(int(len(primes)/4)):
    for j in range(i+1, len(primes)):
        a = primes[i]
        b = primes[j]
        if check(3, 7):
            for k in range(j+1, len(primes)):
                c = primes[k]
                if check(a, c) and check(b, c):
                    for l in range(k+1, len(primes)):
                        d = primes[l]
                        if check(a,d) and check(b, d) and check(c, d):
                            #print("{}, {}, {}, {}, sum: {}".format(a, b, c, d, sum([a,b,c,d])))
                            
                            for t in range(l+1, len(primes)):
                                e = primes[t]
                                
                                if check(a, e) and check(b, e) and check(c, e) and check(d, e):
                                    s = [a, b, c, d, e]
                                    res.append(s)
                                    print("{}, {}, {}, {}, {}, sum: {}".format(a, b, c, d, e, sum(s)))

# 7, 1237, 2341, 12409, 18433, sum: 34427
# 13, 5197, 5701, 6733, 8389, sum: 26033
