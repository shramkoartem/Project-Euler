def pol(n):
    d = list(str(n))
    for i in range(0,len(d)):
        if d[i] != d[-(i+1)]:
            return False
    return True

ten = [i for i in range(1,1000001) if pol(i)]
two = [i for i in ten if pol("{0:b}".format(i))]
sum(two)
