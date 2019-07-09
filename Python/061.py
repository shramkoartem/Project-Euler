def triangle(n):
    return int(n*(n+1)/2)

def square(n):
    return n**2

def penta(n):
    return int(n*(3*n-1)/2)

def hexa(n):
    return int( n*(2*n-1) )

def hepta(n):
    return int( n*(5*n-3)/2 )

def octa(n):
    return int( n*(3*n-2) )
    
    
    
tr = [triangle(i) for i in range(200) if len(str(triangle(i))) == 4]
sq = [square(i) for i in range(200) if len(str(square(i))) == 4]
pe = [penta(i) for i in range(200) if len(str(penta(i))) == 4]
he = [hexa(i) for i in range(200) if len(str(hexa(i))) == 4]
hep = [hepta(i) for i in range(200) if len(str(hepta(i))) == 4]
oc = [octa(i) for i in range(200) if len(str(octa(i))) == 4]

c = tr + sq + pe + he + hep + oc

pairs = []
pa = []

for i in c:
    for j in c:
        if i != j:
            if str(i)[:2] == str(j)[2:] or str(i)[2:] == str(j)[:2]:
                pairs.append([i, j])
                pa.append(i)
                pa.append(j)
                
pa = list(set(pa))

a = pa
b = []

for t in a:
    
    for s in a:
        
        if str(t)[2:] == str(s)[:2]:
        
            for p in a:
                
                if str(s)[2:] == str(p)[:2]:
                
                    for h in a:

                        if str(p)[2:] == str(h)[:2]:

                            for hh in a:

                                if str(h)[2:] == str(hh)[:2]:

                                    for o in a:
                                        
                                        if str(hh)[2:] == str(o)[:2]:
                                            
                                            if str(o)[2:] == str(t)[:2]:
                                                
                                                d = [t, s, p, h, hh, o]
                                                if len(set(d)) == 6:
                                                    b.append([t, s, p, h, hh, o])



for row in b:
    for num in row:
        if num in oc:
            row2 = row[:]
            row2.remove(num)
            for num2 in row2:
                if num2 in hep:
                    
                    row3 = row2[:]
                    row3.remove(num2)
                    
                    for num3 in row3:
                        if num3 in he:
                            row4 = row3[:]
                            row4.remove(num3)
                            for num4 in row4:
                                if num4 in pe:
                                    row5 = row4[:]
                                    row5.remove(num4)
                                    for num5 in row5:
                                        if num5 in sq:
                                            row6 = row5[:]
                                            row6.remove(num5)
                                            if row6[0] in tr: 
                                                print(sum(row))

#28684
