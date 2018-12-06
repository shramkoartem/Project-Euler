def is_prime(n):
    if n == 1:
        return False
    if n%2==0 and n>2:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n%i==0:
            return False
    return True

def factors(n):
    f = []
    for i in range(2, int(n/2)+1):
        if n % i ==0:
                f.append(i)
    return f

def four_primes(n, k):    
    facts = factors(n)
    pf = [i for i in facts if is_prime(i)]
    if len(set(pf))>k:
        return True
    else:
        return False
        
for n in range(134000, 134100):
    ans = []
    print(n)
    for i in range(0,4):
         ans.append(four_primes(n+i,3))
    if all(ans):
        print(" ")
        print(" the right answer!!!      "+str(n))
        break
