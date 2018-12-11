def reversible(n):
    d = str(n)
    if int(d[-1]) == 0:
        return False
    rd  = d[::-1]    
    s = int(d) + int(rd)
    odd = [True if int(i)%2 == 0  else False for i in str(s)]
    if any(odd):
        return False
    return True
    
res = [1 for i in range(1,1000000001) if reversible(i)]
sum(res)
