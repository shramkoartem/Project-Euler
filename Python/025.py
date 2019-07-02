
A = [1]
a, b = 0, 1
while len(str(b))<1000:
    a, b = b, a + b
    A.append(b)
len(A)
