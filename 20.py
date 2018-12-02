from math import *

def factsum(num):
    a = factorial(num)
    A = list(str(a))
    B = sum([int(i) for i in A])
    return B

factsum(10)
27
factsum(100)
648
