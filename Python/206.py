ref = [str(i) for i in range(1,10)]

def check(n):
    digs  = list(str(n))
    for i in range(0,9):
        if digs[i*2] != ref[i]:
            return True
    return False
    
n = 19293949596979899**0.5
while check(n**2): 
    n -= 2
    
print(n*10)
