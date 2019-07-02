def dig_sq(n):
    d = list(str(n))
    d = [int(i)**2 for i in d]
    return sum(d)

count = 0
for n in range(1,10000000):
    while n != 1:
        n = dig_sq(n)
        if n == 89:
            count += 1
            break
count
