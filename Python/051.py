# ugly but works:)

# Step 1. Generate a list of 6-digit prime numbers

def isprime(n):
    if n%2 == 0 and n != 2:
        return False
    
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True
    
candids = [i for i in range(100000,999999) if isprime(i)]

# Step 2. Narrow the search to primes with 3 repeating digits.
#         Last digit can't be repeated since series would then generate non-primes

def check(num,n):
    numstr = list(str(num))[:-1]
    for i in range(10):
        if numstr.count(str(i)) == n:
            return True
    return False
    
checked = [i for i in candids if check(i, 3)]

len(checked)
5495

# Now we have narrowed down our search to 5495 candid solutions. 

def primeseq(num, n):
    l = len(str(num))
    for i in range(l-1):
        for j in range(i, l-1):
            for k in range(j, l-1):
                c = 0
                for d in range(10):
                    numstr = list(str(num))
                    
                    if i == 0 and d == 0:
                        pass
                    else:
                        numstr[i] = numstr[j] = numstr[k] = str(d)
                        a = ''.join(numstr)
                        
                        if isprime(int(a)):
                            c += 1
                            
                    if c == n:
                        return num
                        
ans = [i for i in checked if primeseq(i,8)][0]

#or

i = 0
num = checked[i]
while not primeseq(num, 8):
    i += 1
    num = checked[i]
print(num)
