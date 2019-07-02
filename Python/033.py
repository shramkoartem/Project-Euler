for i in range(10,50):
    for j in range(50,100):
        nom=str(i)
        denom = str(j)
        nm = [int(i) for i in nom]
        dnm = [int(i) for i in denom]
        if 0 not in nm and 0 not in dnm:
            if len(set(nm))>1:
                numbers = []
                for k in nm:
                    if k not in dnm:
                        numbers.append(k)
                for k in dnm:
                    if k not in nm:
                        numbers.append(k)
                try:
                    if max(numbers)/min(numbers) == int(denom) / int(nom):
                        print(str(i)+" / "+str(j))
                except ValueError:
                    pass
                    
16 / 64
19 / 95
26 / 65
49 / 98
