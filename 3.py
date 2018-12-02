from math import sqrt
def f(n):
    fact = []
    lim = int(sqrt(n))+1
    i=2
    for i in range(2,lim):
        if n%i == 0:
            fact.append(i)
            n/=i
        else:
            i+=1
    return fact
    
a = f(600851475143 )
max(a)
