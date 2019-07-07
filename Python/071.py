# a/b < c/d   ==>   a*d < c*b   ==>   b > (a*d)/c

# 1. finding starting value of a
# x/1000000 < 3/7
# x < 3000000/7 = 428572


a = 428572
b = 1000000
c = 3
d = 7

# once the loop stop, we know that the next fraction is lower than 3/7
while a*d > c*b:
    a += -1
    b = round((a*d-1)/c,0)

a += -1
print(a)
