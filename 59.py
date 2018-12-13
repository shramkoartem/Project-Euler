f = open("p059_cipher.txt", "r")
for line in f:
    s = str(line)
s = str(s)[:-1]
s = s.split(",")
s = [int(i) for i in s]


r = []
for a in range(97,123):
    for b in range(97,123):
        for c in range(97,123):
            row = []
            for i in range(0,len(s)-2,3):
                q = [chr(s[i]^a), chr(s[i+1]^b), chr(s[i+2]^c)]
                for j in q:
                    row.append(j)
            r.append(row)

 
