
def divsum(num):
    divisors = []
    for i in range(1, int(num/2)+1):
        if num%i==0:
            divisors.append(i)
    divisors_sum = sum(divisors)
    return [num, divisors_sum]
            
def amicable_nums(start=1, stop=10000):
    global aminums
    aminums=[]
    res = 0
    for i in range(start,stop):
        a = divsum(i)
        b = a[1]
        c = divsum(b)[1]
        if a[0]!=a[1]:
            if a[0]==c:
                if a not in aminums:
                    aminums.append(a)
                    res = res + a[0] + c
                    ans = int(res/2)
    return ans



amicable_nums(stop=10000)
