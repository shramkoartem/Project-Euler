def prime(n):
    if n==1 :
        return False
    if n % 2 == 0 and n>2:
        return False
    
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True
    
diagonals = []
primes = []
fr = 1

n = 0

while fr>0.1:
    n += 1
    
    tr = 4*n**2-2*n+1 #top right
    tl = 4*n**2+1     #top left
    bl = 4*n**2+2*n+1 #bottom left
    br = 4*(n+1)**2-4*(n+1)+1 #bottom right
    
    sq = [tr,tl,bl,br]
    
    for i in sq:
        diagonals.append(i)
        if prime(i):
            primes.append(i)
            
    fr = len(primes)/len(diagonals)
    print(n, fr)

print('result:  ' + str(n*2+1) )
