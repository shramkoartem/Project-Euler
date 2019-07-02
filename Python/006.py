
sumsqr=[]
sqrsum=[]
def sqrdiff(n):
    for i in range(1,n):
        x = i**2
        sumsqr.append(x)
        sqrsum.append(i)
    a = sum(sumsqr)
    b = sum(sqrsum)
    c = b**2
    ans = c-a
    return ans

#ver 2

a = sum([i**2 for i in range(1,101)])
b = sum([i for i in range(1,101)])**2
b-a
