cand = []
for i in range(999,100,-1):
    for j in range(999,100,-1):
        prod = i*j
        cand.append(prod)
res = list(map(str,cand))

new = [i for i in res if len(i)>5]
nine = [i for i in new if i[0]=='9']
out6 = [i for i in nine if i[0]==i[-1] and i[1]==i[-2] and i[2]==i[-3]]
