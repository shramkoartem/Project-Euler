#          / 0 (k>n)
#  p(k,n)={  1 (k=n)
#          \ p(k+1,n)+p(k,n-k) (k<n)


def partitions(k, n):
    if k > n:
        return 0
    elif k == n:
        return 1
    else:
        return partitions(k+1, n) + partitions(k, n-k)
        
ans = partitions(1,100)-1
