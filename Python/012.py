def triang(n):
    global tr
    tr = []
    for i in range(1,n+1):
        A = sum([j for j in range(1,i+1)])
        #for j in range(1,i+1):
        if A not in tr:
            tr.append(A)

triang(10)

def divisors(triangulars):
    for i in triangulars:
        C = []
        for j in range(1,i+1):
            if i%j==0:
                    C.append(j)
        if len(C)>4:
            #return i
            print(i)

divisors(tr)
