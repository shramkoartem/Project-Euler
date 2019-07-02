def is_pent(n):
    i = ((24*n+1)**0.5+1)/6
    try:
        if i.is_integer():
            return True
        else:
            return False
    except AttributeError:
        return False

res = []
for n in range(2000,3000):
    b = int(n*(3*n-1)/2)
    for j in range(1,i):
        a = int(j*(3*j-1)/2)
        if is_pent(a+b) and is_pent(b-a):
            print(b-a)
            print(j)
            print(i)
            break
