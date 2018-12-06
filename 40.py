d = "".join([str(i) for i in range(1,1000000)])

ans = 1
ten = 1
for i in range(0,6):
    a = int(d[ten-1])
    ans = ans*a
    ten = ten*10
ans
