#Correct solution

A = [0]
a, b = 0, 1
for i in A:
        a, b = b, a + b
        A.append(b)
        y = len(A)-1
        if A[y]>4000000:
            break
        else:
            continue

del(A[-1])

b = []
for i in A:
    if i%2==0:
      b.append(i)
sum(b)
