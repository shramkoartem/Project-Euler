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
    b = round((a*d-1)/c,0)+1

a += -1
print(a)


# aletranitevy with pyspark

from pyspark import SparkContext
sc = SparkContext()

def b(a):
    return int((a*7-1)/3)+1

rdd = sc.parallelize([[a, b(a)] for a in range(428572,1,-1) if a*7 < b(a)*3] and b(a)<1000000)

rdd.collect()[0]

