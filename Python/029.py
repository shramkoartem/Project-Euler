res = [[a**b for b in range(2,101)] for a in range(2,101)]

new = []
for row in res:
    for i in row:
        new.append(i)
len(set(new))
