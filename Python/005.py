from fractions import gcd
def lcm(a,b):
    "Calculate the lowest common multiple of two integers a and b"
    return a*b//gcd(a,b)

from functools import reduce
reduce(lcm, range(1,20+1))
